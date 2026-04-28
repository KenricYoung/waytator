%bcond_with tests
%global forgeurl https://github.com/faetalize/waytator
%global version0 1.2.3
%forgemeta
Name:            waytator
Version:         %{forgeversion}
Release:         %{autorelease}
Summary:         A screenshot annotator and lightweight image editor

License:         GPL-3.0-or-later
URL:             %{forgeurl}
Source0:         %{forgesource0}

BuildRequires:   meson
BuildRequires:   gcc
BuildRequires:   pkgconfig(gtk4) pkgconfig(libadwaita-1)

Recommends:      tesseract

%description
waytator is a screenshot annotator and lightweight image editor

%package         niri
Summary:         niri helper scripts

Requires(meta):  %{name}%{?_isa}
Requires:        bash
Requires:        niri
Requires:        jq
Requires:        util-linux-core
Requires:        (coreutils or coreutils-single)

Recommends:      wl-clipboard

%description     niri
waytator helper script for niri users
View the README.md for more documemtation

%prep
%forgeautosetup

%conf
%meson

%build
%meson_build

%install
%meson_install
install --target-directory %{buildroot}%{_bindir} scripts/screenshot-to-waytator.sh

%if %{with tests}
%check
%meson_test
%endif

%files
%{_bindir}/waytator
%{_datadir}/applications/dev.faetalize.waytator.desktop
%{_datadir}/icons/*
%license LICENSE
%doc README.md

%files niri
%{_bindir}/screenshot-to-waytator.sh

%changelog
%autochangelog
