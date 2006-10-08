Summary:	New Linux virtual server utilities
Summary(pl):	Nowe narzêdzia dla linuksowych serwerów wirtualnych (vserver)
Name:		vserver-utils
Version:	1.0.3
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dev.gentoo.org/~hollow/vserver-utils/%{name}-%{version}.tar.gz
# Source0-md5:	5359a8ac6e423f883beb49bb1f376e73
URL:		http://dev.croup.de/proj/vserver-utils/
BuildRequires:	libvserver-devel >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
New Linux virtual server utilities.

%description -l pl
Nowe narzêdzia dla linuksowych serwerów wirtualnych (vserver).

%prep
%setup -q
%configure \
	--disable-dietlibc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

chmod 755 $RPM_BUILD_ROOT/vservers
mkdir -p  $RPM_BUILD_ROOT/var/lock/vservers

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/vserver-utils
%attr(755,root,root) %{_libdir}/vserver-utils/lockfile
%attr(755,root,root) %{_sbindir}/nidof
%attr(755,root,root) %{_sbindir}/vattr
%attr(755,root,root) %{_sbindir}/vcontext
%attr(755,root,root) %{_sbindir}/vdlimit
%attr(755,root,root) %{_sbindir}/vexec
%attr(755,root,root) %{_sbindir}/vflags
%attr(755,root,root) %{_sbindir}/vinfo
%attr(755,root,root) %{_sbindir}/vkill
%attr(755,root,root) %{_sbindir}/vlimit
%attr(755,root,root) %{_sbindir}/vlogin
%attr(755,root,root) %{_sbindir}/vmount
%attr(755,root,root) %{_sbindir}/vnamespace
%attr(755,root,root) %{_sbindir}/vncontext
%attr(755,root,root) %{_sbindir}/vnflags
%attr(755,root,root) %{_sbindir}/vps
%attr(755,root,root) %{_sbindir}/vpstree
%attr(755,root,root) %{_sbindir}/vrsetup
%attr(755,root,root) %{_sbindir}/vsched
%attr(755,root,root) %{_sbindir}/vserver
%attr(755,root,root) %{_sbindir}/vtop
%attr(755,root,root) %{_sbindir}/vuname
%attr(755,root,root) %{_sbindir}/vwait
%attr(755,root,root) %{_sbindir}/xidof
%dir %{_datadir}/vserver-utils
%dir %{_datadir}/vserver-utils/commands
%dir %{_datadir}/vserver-utils/defaults
%dir %{_datadir}/vserver-utils/examples
%dir %{_datadir}/vserver-utils/lib
%{_datadir}/vserver-utils/commands/*.sh
%{_datadir}/vserver-utils/defaults/*
%{_datadir}/vserver-utils/examples/*
%{_datadir}/vserver-utils/lib/*.sh
%{_datadir}/vserver-utils/pathconfig
%dir %attr(000,root,root) /vservers
%dir %attr(700,root,root) /var/lock/vservers
