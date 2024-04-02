Name:           stillos-settings
Version:        40
Release:        16%{?dist}
Summary:        Default settings for stillOS

License:        Unlicense
URL:            https://github.com/ProjectStill/StillReleaseRPMs

Source0:	00_stillos.gschema.override
Source1:	LICENSE
Requires:	adw-gtk3-theme

BuildArch:  noarch

%description
stillOS Settings

%build
%install
mkdir -p %{buildroot}%{_datarootdir}/glib-2.0/schemas
cp %{SOURCE0} %{buildroot}%{_datarootdir}/glib-2.0/schemas/00_stillos.gschema.override

%files
%{_datarootdir}/glib-2.0/schemas/00_stillos.gschema.override

%changelog
* Thu Jul 13 2023 PizzaLovingNerd
- stillOS

* Wed Mar 9 2022 PizzaLovingNerd
- Removed GNOME Session, now it's just GNOME settings

* Fri Feb 25 2022 PizzaLovingNerd
- Fixed GNOME Shell Theme
- Fixed Wayland session not showing up
- Fixed Settings not working.

* Wed Aug 11 2021 PizzaLovingNerd
- Spec file built
