Summary:	Menu Style Configuration
Name:		drakmenustyle
Version:	0.14.1
Release:	14
License:	GPLv2
Group:		System/Configuration/Other
Url:		%{disturl}
Source0:	%{name}-%{version}.tar.bz2
Source1:	drakmenustyle16.png
Source2:	drakmenustyle32.png
Source3:	drakmenustyle48.png
BuildArch:	noarch

BuildRequires:	perl-MDK-Common-devel
Requires:	drakxtools
Requires:	perl-Gtk2
Provides:	menudrake

%description
Drakmenustyle enables to configure the menu style under %{distribution}.

%prep
%setup -q

%build
sed -i -e 's/^use strict/#use strict/g' drakmenustyle

%install
%makeinstall_std

#install lang
%find_lang %{name}

#install menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-drakmenustyle.desktop << EOF
[Desktop Entry]
Name=Menu Style Configuration
Comment=Menu Style Configuration
Exec=%{_bindir}/%{name}
Icon=drakmenustyle
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;X-MandrivaLinux-CrossDesktop;Settings;
NoDisplay=true
EOF

#install menu icon
mkdir -p %buildroot/{%{_miconsdir},%{_liconsdir}}
install -m644 %SOURCE1 %buildroot/%{_miconsdir}/drakmenustyle.png
install -m644 %SOURCE2 %buildroot/%{_iconsdir}/drakmenustyle.png
install -m644 %SOURCE3 %buildroot/%{_liconsdir}/drakmenustyle.png

%files -f %{name}.lang
%doc COPYING ChangeLog
%{_bindir}/*
%{_datadir}/applications/mandriva-drakmenustyle.desktop
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png

