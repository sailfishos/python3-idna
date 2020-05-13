Name:       python3-idna
Summary:    Internationalized Domain Names in Applications
Version:    2.9
Release:    1
License:    BSD
URL:        https://pypi.org/project/idna/
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Support for the Internationalised Domain Names in Applications (IDNA) protocol as specified in RFC 5891. This is the latest version of the protocol and is sometimes referred to as “IDNA 2008”.

This library also provides support for Unicode Technical Standard 46, Unicode IDNA Compatibility Processing.

This acts as a suitable replacement for the “encodings.idna” module that comes with the Python standard library, but only supports the old, deprecated IDNA specification (RFC 3490).

%prep
%setup -q -n %{name}-%{version}/idna

%build
%{py3_build}

%install
rm -rf %{buildroot}
%{py3_install}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/idna
%{python3_sitearch}/idna-*.egg-info
