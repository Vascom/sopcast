Name:           sopcast       
Version:        3.2.6
Release:        3%{?dist}.R
Summary:        A P2P Stream program

License:        Redistributable
URL:            http://www.sopcast.org
Group:          Applications/Internet
Source0:        http://download.easetuner.com/download/sp-auth.tgz
Source1:        sopcast
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:       mplayer      


%description
A P2P Stream program and playing script    


%prep
%setup -q -n sp-auth


%build
rm -rf $RPM_BUILD_ROOT


%install
mkdir -p %{buildroot}%{_bindir}
%{__install} -pD -m755 sp-sc-auth %{buildroot}%{_bindir}
# File install
%{__install} -pD -m755 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_bindir}/sopcast

%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc Readme
%defattr(-,root,root)
%{_bindir}/*



%changelog
* Tue Jul 12 2011 Vasiliy N. Glazov <vascom2@gmail.com> 3.2.6-3.R
- updated to 3.2.6
- added playing script

* Mon May 19 2008 Arkady L. Shane <ashejn@yandex-team.ru> 1.1.1-2
- fixed bug #12

* Sun May 18 2008 Arkady L. Shane <ashejn@yandex-team.ru> 1.1.1-1
- initial build for Fedora
