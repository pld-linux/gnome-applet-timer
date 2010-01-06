%define		realname	timer-applet
Summary:	Timer Applet - a countdown timer applet for the GNOME panel
Summary(pl.UTF-8):	Timer Applet - aplet zegarka odliczającego zadany czas dla panelu GNOME
Name:		gnome-applet-timer
Version:	2.0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/timerapplet/%{realname}-%{version}.tar.gz
# Source0-md5:	c56e5ec73ece83389e05a51aa38e0d59
URL:		http://timerapplet.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-panel-devel >= 2.6
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.197
%pyrequires_eq	python-modules
%pyrequires_eq	python
Requires:	gnome-panel >= 2.6
Requires:	python-dbus >= 0.80.2
Requires:	python-pynotify
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/gconf

%description
Highlights:
 - Add multiple Timer Applets to the panel to have different timers
   running simultaneously
 - Quickly set a time and the applet will notify you when time's up
 - Create presets for quick access to frequently-used times
 - Small and unobtrusive. Choose to either view the remaining time
   right in the panel or hide it so you don't get distracted by the
   countdown. You can still view the remaining time by hovering your
   mouse over the timer icon
 - User interface follows the GNOME Human Interface Guidelines

%description -l pl.UTF-8
Możliwości:
 - dodawanie do panelu wielu apletów zegarka w celu uruchamiania ich
   jednocześnie
 - szybkie ustawianie czasu, po którym aplet ma powiadomić
 - tworzenie predefiniowanych ustawień dla często używanych czasów
 - mały i nienatarczywy: można wybrać między widokiem pozostałego
   czasu w panelu albo ukryć go, aby nie być rozpraszanym widokiem
   mijanego czasu; pozostały czas można podejrzeć zatrzymując kursor
   myszy nad ikoną zegarka
 - interfejs użytkownika zgodny z GNOME HIG

%prep
%setup -q -n %{realname}-%{version}

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--with-gconf-schema-file-dir=%{_sysconfdir}/schemas
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean
%find_lang %{realname} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install %{realname}.schemas

%preun
%gconf_schema_uninstall %{realname}.schemas

%files -f %{realname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/%{realname}
%{_sysconfdir}/schemas/%{realname}.schemas
%{_libdir}/bonobo/servers/TimerApplet.server
%{_datadir}/%{realname}
%{_pixmapsdir}/%{realname}.png
%{py_sitescriptdir}/timerapplet
