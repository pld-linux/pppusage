#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
Summary:	Tool to create PPP connections summary
Summary(pl.UTF-8):	Narzędzie do tworzenia statystyk połączeń PPP
Name:		pppusage
Version:	0.2.5
Release:	2
License:	BSD
Group:		Applications/Console
Source0:	http://code.jhweiss.de/pppusage/%{name}-%{version}.tar.gz
# Source0-md5:	7cf370d5b147ff084025234c43d01a45
URL:		http://code.jhweiss.de/pppusage/
Patch0:		%{name}-config.patch
Patch1:		%{name}-Makefile_PL.patch
%if %{with tests}
BuildRequires:	perl-DB_File
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pppusage summarizes average and total transfer volumes, number of
connections, and average and total online time for PPP connections.
The data is collected by reading the syslog files which contain the
ppp[d] messages. A database file is used to store the relevant data.
Certain time ranges (that is: a year, month, or day) may be specified
on the command line.

%description -l pl.UTF-8
pppusage podsumowuje wielkości średniego i całkowitego transferu,
liczbę połączeń oraz średni i całkowity czas dla połączeń PPP. Dane są
zbierane poprzez czytanie plików sysloga zawierających komunikaty
ppp[d]. Do przechowywania danych używany jest plik z bazą. Określone
przedziały czasu (tzn. rok, miesiąc, dzień) można podać z linii
poleceń.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	SYSCONFDIR="%{_sysconfdir}"

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install -d $RPM_BUILD_ROOT%{_var}/lib/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes License README TODO UPGRADE
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/PPPUsage
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}rc
%{_mandir}/man1/%{name}.*
%dir %{_var}/lib/%{name}
