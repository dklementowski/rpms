%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     it87-frankcrawford
Version:  1
Release:  4%{?dist}
Summary:  Linux Driver for ITE LPC chips
License:  none
URL:      https://github.com/frankcrawford/it87
Source1:   ./it87.conf

# For kmod package
Provides:       %{name}-kmod-common = %{version}-%{release}
Requires:       %{name}-kmod >= %{version}

BuildArch:      noarch
BuildRequires:  systemd-rpm-macros

%description
Linux Driver for ITE LPC chips

%prep

%build

%install
%if %{defined _modulesloaddir}
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_modulesloaddir}/%{name}.conf
%endif

%files
%if %{defined _modulesloaddir}
%{_modulesloaddir}/%{name}.conf
%endif

%changelog
{{{ git_dir_changelog }}}
