Summary:	X11 drivers for Poulsbo (psb) 3D acceleration
Name:		xpsb-glx
Version:	0.18
Release:	6%{?dist}
License:	Redistributable, no modification permitted
Group:		System Environment/Kernel
URL:		http://ppa.launchpad.net/ubuntu-mobile/ubuntu/pool/main/x/xpsb-glx/
Source0:	http://ppa.launchpad.net/ubuntu-mobile/ubuntu/pool/main/x/xpsb-glx/%{name}_%{version}.orig.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExclusiveArch:	i686

%description
This package contains the 3D X11 drivers for the Poulsbo (psb) graphics
subsystem.

%prep
%setup -q -n %{name}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/dri
mkdir -p %{buildroot}%{_libdir}/va/drivers
mkdir -p %{buildroot}%{_libdir}/xorg/modules/drivers

install -m 0644 drivers/* %{buildroot}%{_libdir}/xorg/modules/drivers
install -m 0644 dri/psb_dri.so %{buildroot}%{_libdir}/dri
install -m 0644 dri/psb_drv_video.so %{buildroot}%{_libdir}/va/drivers

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/xorg/modules/drivers/*
%{_libdir}/va/drivers/*
%{_libdir}/dri/*

%changelog
* Thu Oct 14 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.18-6
- Rebuilt for gcc bug

* Wed Sep 30 2009 Adam Williamson <adamwill AT shaw DOT ca> - 0.18-5
- change my email address in changelog to correct one for Fusion

* Mon Aug 24 2009 Adam Williamson <adamwill AT shaw DOT ca> - 0.18-4
- exclusivearch i686 (most accurate we can get)

* Wed Aug 19 2009 Adam Williamson <adamwill AT shaw DOT ca> - 0.18-3
- correct license for RPMFusion conventions

* Wed Aug 12 2009 Adam Williamson <adamwill AT shaw DOT ca> - 0.18-2
- Put the video playback acceleration driver where libva will find it

* Mon Aug 10 2009 Adam Williamson <adamwill AT shaw DOT ca> - 0.18-1
- Begin changelog tracking
