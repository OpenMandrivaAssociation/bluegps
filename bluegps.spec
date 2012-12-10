Name: bluegps
Version: 2.0
Group: Sciences/Geosciences
Release: %mkrel 5
Summary: Simple command line tool for the Royaltek RBT-3000 bluetooth GPS receiver
License: GPL
URL: http://www.harbaum.org/till/bluegps/
Source: http://www.harbaum.org/till/bluegps/bluegps-linux-%{version}.tgz
BuildRequires: bluez-devel
BuildRoot: %{_tmppath}/%{name}-root

%description
BlueGPS is a simple command line tool to download datalogs from the Royaltek
RBT-3000 bluetooth GPS receiver under Linux, and to configure the data logger.

%prep
%setup -q -n %{name}-linux-%{version}

%build
%make

%install
rm -Rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
install -m755 bluegps %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
install -m644 bluegps.1 %{buildroot}/%{_mandir}/man1

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%doc %{_mandir}/man1/%{name}*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0-5mdv2011.0
+ Revision: 616781
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 2.0-4mdv2010.0
+ Revision: 436863
- rebuild

* Tue Mar 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0-3mdv2009.1
+ Revision: 347692
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.0-2mdv2009.0
+ Revision: 266277
- rebuild early 2009.0 package (before pixel changes)

* Sun Jun 08 2008 Buchan Milne <bgmilne@mandriva.org> 2.0-1mdv2009.0
+ Revision: 216997
- import bluegps


* Sun Jun 08 2008 Buchan Milne <bgmilne@mandriva.org> 2.0-1mdv
- Initial package
