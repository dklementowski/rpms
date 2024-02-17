Name:     it87
Version:  154
Release:  2%{?dist}
Summary:  Linux Driver for ITE LPC chips
License:  none
URL:      https://github.com/frankcrawford/it87
Source1:   ./it87.conf

# For kmod package
Provides:       %{name}-kmod-common = %{version}-%{release}
Requires:       %{name}-kmod >= %{version}

BuildArch:      noarch

%description
Linux Driver for ITE LPC chips

%prep

%build

%install
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_modulesloaddir}/%{name}.conf

%files
%{_modulesloaddir}/%{name}.conf

%changelog
