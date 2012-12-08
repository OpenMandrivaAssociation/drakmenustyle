

Summary:  Menu Style Configuration
Name:     drakmenustyle
Version:  0.14.1
Release:  %mkrel 6
Source0:  %name-%version.tar.bz2
Source1:  drakmenustyle16.png
Source2:  drakmenustyle32.png
Source3:  drakmenustyle48.png
License:  GPL
Group:    System/Configuration/Other
Url:      http://www.mandrivalinux.com/en/cvs.php3
BuildRequires: perl-MDK-Common-devel
Requires: drakxtools => 10.4.53-1mdv2007.0
Requires: perl-Gtk2 >= 1.023-1mdk
BuildRoot: %_tmppath/%name-%version-buildroot
Provides: menudrake
Obsoletes: menudrake
BuildArch: noarch

%description
Drakmenustyle enables to configure the menu style under Mandriva Linux.

%prep
%setup -q

%build
perl -pi -e 's/^use strict/#use strict/g' drakmenustyle

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall_std

#install lang
%find_lang %name

#install menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-drakmenustyle.desktop << EOF
[Desktop Entry]
Name=Menu Style Configuration
Comment=Menu Style Configuration
Exec=%{_bindir}/%name
Icon=drakmenustyle
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;X-MandrivaLinux-CrossDesktop;Settings;
NoDisplay=true
EOF

#install menu icon
mkdir -p %buildroot/{%_miconsdir,%_liconsdir}
install -m644 %SOURCE1 %buildroot/%_miconsdir/drakmenustyle.png
install -m644 %SOURCE2 %buildroot/%_iconsdir/drakmenustyle.png
install -m644 %SOURCE3 %buildroot/%_liconsdir/drakmenustyle.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING ChangeLog
%_bindir/*
%{_datadir}/applications/mandriva-drakmenustyle.desktop
%_miconsdir/*.png
%_iconsdir/*.png
%_liconsdir/*.png




%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.14.1-5mdv2011.0
+ Revision: 663858
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.14.1-4mdv2011.0
+ Revision: 604822
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.14.1-3mdv2010.1
+ Revision: 522509
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.14.1-2mdv2010.0
+ Revision: 413383
- rebuild

* Wed Apr 15 2009 Thierry Vignaud <tv@mandriva.org> 0.14.1-1mdv2009.1
+ Revision: 367390
- updated translation

* Mon Mar 30 2009 Thierry Vignaud <tv@mandriva.org> 0.14-1mdv2009.1
+ Revision: 362304
- updated translation

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.13-2mdv2009.1
+ Revision: 350839
- rebuild

* Mon Sep 22 2008 Thierry Vignaud <tv@mandriva.org> 0.13-1mdv2009.0
+ Revision: 286969
- updated translation

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.12-1mdv2009.0
+ Revision: 218424
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Apr 03 2008 Thierry Vignaud <tv@mandriva.org> 0.12-1mdv2008.1
+ Revision: 192100
- updated translation

* Tue Mar 25 2008 Thierry Vignaud <tv@mandriva.org> 0.11-2mdv2008.1
+ Revision: 190092
- updated translation

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.10-2mdv2008.1
+ Revision: 149261
- rebuild
- drop old menu
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Oct 01 2007 Thierry Vignaud <tv@mandriva.org> 0.10-1mdv2008.0
+ Revision: 94269
- updated translation

* Tue Sep 25 2007 Thierry Vignaud <tv@mandriva.org> 0.9-1mdv2008.0
+ Revision: 92937
- updated translations

* Tue Sep 18 2007 Thierry Vignaud <tv@mandriva.org> 0.8-2mdv2008.0
+ Revision: 89788
- hide menu entry\n- do not hardcode icon extension

* Sat Sep 15 2007 Thierry Vignaud <tv@mandriva.org> 0.8-1mdv2008.0
+ Revision: 86871
- translation snapshot

* Mon Sep 03 2007 Thierry Vignaud <tv@mandriva.org> 0.7-1mdv2008.0
+ Revision: 78536
- kill discovery choice (#33073)
- translation snapshot
- replace X-MandrivaLinux-System-Configuration by X-MandrivaLinux-CrossDesktop

* Fri Jun 08 2007 Thierry Vignaud <tv@mandriva.org> 0.6-1mdv2008.0
+ Revision: 37429
- first release after SVN recover


* Mon Mar 12 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.5-1mdv2007.1
+ Revision: 141865
- Import drakmenustyle

* Mon Mar 12 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.5-1mdv2007.1
- translation snapshot

* Sun Sep 17 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.4-1mdv2007.0
- updated translations

* Wed Sep 13 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.3-1mdv2007.0
- actually use translations
- updated translations

* Wed Sep 06 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.2-1mdv2007.0
- don't display the banner when embedded
- fix summary (#24959)
- HIG
- new icons

* Fri Aug 18 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.1-1mdv2007.0
- initial release

