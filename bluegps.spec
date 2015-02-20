%define debug_package	%{nil}

Name: bluegps
Version: 2.0
Group: Sciences/Geosciences
Release: 6
Summary: Simple command line tool for the Royaltek RBT-3000 bluetooth GPS receiver
License: GPL
URL: http://www.harbaum.org/till/bluegps/
Source: http://www.harbaum.org/till/bluegps/bluegps-linux-%{version}.tgz
BuildRequires: bluez-devel


%description
BlueGPS is a simple command line tool to download datalogs from the Royaltek
RBT-3000 bluetooth GPS receiver under Linux, and to configure the data logger.

%prep
%setup -q -n %{name}-linux-%{version}

%build
%make

%install
mkdir -p %{buildroot}/%{_bindir}
install -m755 bluegps %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
install -m644 bluegps.1 %{buildroot}/%{_mandir}/man1


%files
%{_bindir}/%{name}
%doc %{_mandir}/man1/%{name}*


