Summary:	Tool to create PPP connections summary
Summary(pl):	Narzêdzie do tworzenia statystyk po³±czeñ PPP
Name:		pppusage
Version:	0.2.5
Release:	0.1
License:	BSD	
Group:		Applications/Console
Source0:	http://code.jhweiss.de/pppusage/pppusage-0.2.5.tar.gz
# Source0-md5:	7cf370d5b147ff084025234c43d01a45
URL:		http://code.jhweiss.de/pppusage/
BuildRequires:	%{__perl}
Requires:	perl-modules
Requires:	perl-DB_File
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pppusage summarizes average and total transfer volumes, number of
connections, and average and total online time for PPP connections. The
data is collected by reading the syslog files which contain the ppp[d]
messages. A database file is used to store the relevant data. Certain
time ranges (that is: a year, month, or day) may be specified on the
command line.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	SYSCONFDIR="%{_sysconfdir}" \
	INST_SYSCONFDIR="$RPM_BUILD_ROOT%{_sysconfdir}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man1,%{perl_vendorlib}/PPPUsage}

install etc/pppusagerc		$RPM_BUILD_ROOT%{_sysconfdir}
install bin/pppusage		$RPM_BUILD_ROOT%{_bindir}
install blib/man1/pppusage.1p	$RPM_BUILD_ROOT%{_mandir}/man1
install lib/PPPUsage/*		$RPM_BUILD_ROOT%{perl_vendorlib}/PPPUsage

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README TODO UPGRADE
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}rc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}.*
%{perl_vendorlib}/PPPUsage/*.pm
