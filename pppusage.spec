#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Tool to create PPP connections summary
Summary(pl):	Narzêdzie do tworzenia statystyk po³±czeñ PPP
Name:		pppusage
Version:	0.2.5
Release:	1
License:	BSD	
Group:		Applications/Console
Source0:	http://code.jhweiss.de/pppusage/%{name}-%{version}.tar.gz
# Source0-md5:	7cf370d5b147ff084025234c43d01a45
URL:		http://code.jhweiss.de/pppusage/
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

%description -l pl
pppusage podsumowuje wielko¶ci ¶redniego i ca³kowitego transferu,
liczbê po³±czeñ oraz ¶redni i ca³kowity czas dla po³±czeñ PPP. Dane s±
zbierane poprzez czytanie plików sysloga zawieraj±cych komunikaty
ppp[d]. Do przechowywania danych u¿ywany jest plik z baz±.
Okre¶lone przedzia³y czasu (tzn. rok, miesi±c, dzieñ) mo¿na podaæ z
linii poleceñ.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	SYSCONFDIR="%{_sysconfdir}" \
	INST_SYSCONFDIR="$RPM_BUILD_ROOT%{_sysconfdir}"

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes License README TODO UPGRADE
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/PPPUsage
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}rc
%{_mandir}/man1/%{name}.*
