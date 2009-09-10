Name: bluegps
Version: 2.0
Group: Sciences/Geosciences
Release: %mkrel 4
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

