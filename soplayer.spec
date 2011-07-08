Name:           soplayer           
Version:        0.1
Release:        1%{?dist}.R
Summary:        Useful player to view sopcast broadcasts

License:        GPLv2
URL:            https://github.com/Vascom/soplayer
Source0:        soplayer


Requires:       mplayer
Requires:       sopcast      


BuildArch:      noarch


%description
Useful player to view sopcast broadcasts    


%prep
echo "Nothing to prep"


%build
echo "Nothing to build"


%install
rm -rf $RPM_BUILD_ROOT

# File install
%{__install} -pD -m644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_bindir}/soplayer

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(755,root,root)
%config(noreplace) %{_bindir}/soplayer


%doc


%changelog
* Fri Jul  08 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.1-1.R
- initial build
