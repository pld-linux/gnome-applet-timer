Name:           timer-applet
Version:        1.0
Release:        1
Summary:        Timer Applet Icon Timer Applet is a countdown timer applet for the GNOME panel.

Group:          User Interface/Desktops
License:        GPL
URL:            http://timerapplet.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/timerapplet/timer-applet-1.0.tar.gz
#Source99:       <for original Red Hat or upstream spec as *.spec.upstream>
#Patch0:         
#Patch1:         
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gnome-panel-devel >= 2.6
Requires:       gnome-panel >= 2.6

%description
Highlights:

    * Add multiple Timer Applets to the panel to have different timers running simultaneously
    * Quickly set a time and the applet will notify you when time's up
    * Create presets for quick access to frequently-used times
    * Small and unobtrusive. Choose to either view the remaining time right in the panel or hide it so you don't get distracted by the countdown. You can still view the remaining time by hovering your mouse over the timer icon
    * User interface follows the GNOME Human Interface Guidelines

Translations: Basque, French, German, Spanish, Swedish

#%package        devel
#Summary:        
#Group:          Development/Libraries
#Requires:       %{name} = %{version}-%{release}

#%description    devel
#<Long description of subpackage here>
#<Multiple lines are fine>


%prep
%setup -q


%build
# For QT apps: [ -n "$QTDIR" ] || . %{_sysconfdir}/profile.d/qt.sh
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
# For GConf apps: prevent schemas from being installed at this stage
#export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
# Note: the find_lang macro requires gettext
%find_lang %{name}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%check || :
#make test
#make check


%clean
rm -rf $RPM_BUILD_ROOT


# ldconfig's for packages that install %{_libdir}/*.so.*
# -> Don't forget Requires(post) and Requires(postun): /sbin/ldconfig
# ...and install-info's for ones that install %{_infodir}/*.info*
# -> Don't forget Requires(post) and Requires(preun): /sbin/install-info

%post
/sbin/ldconfig
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :
# For GConf apps: install schemas as system default
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
  %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null

%preun
if [ $1 -eq 0 ]; then
  /sbin/install-info --delete %{_infodir}/%{name}.info \
    %{_infodir}/dir 2>/dev/null || :
fi
# For GConf apps: uninstall app's system default schemas
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-uninstall-rule \
  %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :

%postun -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
#%{_libdir}/*.so.*
%{_libdir}/bonobo/servers/GNOME_TimerApplet.server
#%{_datadir}/%{name}
%{_datadir}/gnome-2.0/ui/GNOME_TimerApplet.xml
#%{_datadir}/locale/
%{_datadir}/pixmaps/%{name}
%{_datadir}/gnome/help/%{name}
#%{_mandir}/man[^3]/*

#%files devel
#%defattr(-,root,root,-)
#%doc HACKING
#%{_libdir}/*.a
#%{_libdir}/*.so
#%{_mandir}/man3/*


%changelog
* Sun Apr 03 2005 Christoph Wickert <christroph.wickert@web.de> - (0:)1.0-fc3_cw.1
- Updated to version 1.0.

* Thu Mar 24 2005 Christoph Wickert <christroph.wickert@web.de> - (0:)0.9-fc3_cw.1
- Updated to version 0.9.

* Mon Mar 21 2005 Christoph Wickert <christroph.wickert@web.de> - (0:)0.8-fc3_cw.1
- Initial RPM release.
