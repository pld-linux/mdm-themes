Summary:	Default MDM themes
Summary(pl.UTF-8):	Domyślne motywy MDM
Name:		mdm-themes
Version:	0
%define	gitref	3417d5641aca697071bb35b5ec585dd9bdca9e07
%define	snap	20141002
Release:	0.%{snap}.1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://github.com/linuxmint/mdm-themes/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	7fe85e7019a4e9bc8b8fb4c24d629df8
URL:		https://github.com/linuxmint/mdm-themes
Requires:	mdm >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Themes for the MDM display manager.

%description -l pl.UTF-8
Motywy dla zarządcy ekranów MDM.

%prep
%setup -q -n %{name}-%{gitref}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

cp -pr usr $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc debian/changelog
%{_datadir}/mdm/html-themes/mdm
