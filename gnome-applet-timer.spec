Summary:	Timer Applet - a countdown timer applet for the GNOME panel
Summary(pl):	Timer Applet - aplet zegarka odliczajacego zadany czas dla panelu GNOME
Name:		timer-applet
Version:	1.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/timerapplet/%{name}-%{version}.tar.gz
# Source0-md5:	63b40b8ae59e12d2f7068ebf64fffd86
URL:		http://timerapplet.sourceforge.net/
BuildRequires:	gnome-panel-devel >= 2.6
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	gnome-panel >= 2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl
Mo¿liwo¶ci:
 - dodawanie do panelu wielu apletów zegarka w celu uruchamiania ich
   jednocze¶nie
 - szybkie ustawianie czasu, po którym aplet ma powiadomiæ
 - tworzenie predefiniowanych ustawieñ dla czêsto u¿ywanych czasów
 - ma³y i nienatarczywy: mo¿na wybraæ miêdzy widokiem pozosta³ego
   czasu w panelu albo ukryæ go, aby nie byæ rozpraszanym widokiem
   mijanego czasu; pozosta³y czas mo¿na podejrzeæ zatrzymuj±c kursor
   myszy nad ikon± zegarka
- interfejs u¿ytkownika zgodny z GNOME HIG

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install %{name}.schemas

%preun
%gconf_schema_uninstall %{name}.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_libdir}/bonobo/servers/GNOME_TimerApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_TimerApplet.xml
%{_pixmapsdir}/%{name}
%{_datadir}/gnome/help/%{name}
