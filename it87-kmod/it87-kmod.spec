%if 0%{?fedora}
%global buildforkernels akmod
%global debug_package %{nil}
%endif

Name:     it87-kmod
Version:  155
Release:  2%{?dist}
Summary:  Linux Driver for ITE LPC chips
License:  none
URL:      https://github.com/frankcrawford/it87
Source:   %{url}/archive/refs/heads/master.zip

BuildRequires: kmodtool git binutils

%{expand:%(kmodtool --target %{_target_cpu} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Linux Driver for ITE LPC chips

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool --target %{_target_cpu} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%setup -q -c it87-master

for kernel_version  in %{?kernel_versions} ; do
  cp -a it87-master _kmod_build_${kernel_version%%___*}
done

%build
mkdir /tmp/bin
export PATH=$PATH:/tmp/bin
ln -s /usr/bin/ld.bfd /tmp/bin/ld
for kernel_version  in %{?kernel_versions} ; do
  make V=1 %{?_smp_mflags} -C ${kernel_version##*___} M=${PWD}/_kmod_build_${kernel_version%%___*} VERSION=v%{version} modules
done
rm -r /tmp/bin

%install
for kernel_version in %{?kernel_versions}; do
 mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 install -D -m 755 _kmod_build_${kernel_version%%___*}/it87.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 chmod a+x %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/it87.ko
done
%{?akmod_install}

%changelog
