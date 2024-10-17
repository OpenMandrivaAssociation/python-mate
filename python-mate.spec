%define	oname	python

Summary:	The sources for the PyMATE Python extension module
Name:		python-mate
Version:	1.4.0
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/GNOME
URL:		https://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/python-mate-%{version}.tar.xz

BuildRequires:	mate-common
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libmate-2.0)
BuildRequires:	pkgconfig(libmateui-2.0)
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(pymatecorba-2)
BuildRequires:	pkgconfig(python)
BuildRequires:	libgcrypt-devel

Requires:	libmate
Requires:	libmateui
Requires:	pygtk2.0
Requires:	%{oname}-matecomponent

%description
The python-mate package contains the source packages for the Python
bindings for MATE called PyMATE.

PyMATE is an extension module for Python that provides access to the
base MATE libraries, so you have access to more widgets, a simple
configuration interface, and metadata support.

%package -n %{oname}-matecanvas
Summary:	Python bindings for the MATE Canvas
Group:		Graphical desktop/GNOME
Requires:	libmatecanvas
Requires:	pygtk2.0
Requires:	%{name} = %{version}

%description -n %{oname}-matecanvas
This module contains a wrapper that allows use of the MATE Canvas
in Python.

%package -n %{oname}-matecomponent
Summary:	Python bindings for interacting with matecomponent
Group:		Graphical desktop/GNOME
Requires:	libmatecomponent
Requires:	%{oname}-matecanvas = %{version}
Requires:	python-corba

%description -n %{oname}-matecomponent
This module contains a wrapper that allows the creation of matecomponent
components and the embedding of matecomponent components in Python.

%package -n %{oname}-mateconf
Summary:	Python bindings for interacting with mate-conf
Group:		Graphical desktop/GNOME
Requires:	mate-conf

%description -n %{oname}-mateconf
This module contains a wrapper that allows the use of mate-conf via Python.

%package -n %{oname}-matevfs
Summary:	Python bindings for interacting with mate-vfs
Group:		Graphical desktop/GNOME
Requires:	mate-vfs

%description -n %{oname}-matevfs
This module contains a wrapper that allows the use of mate-vfs via python.

%package devel
Summary:	Development files of %{name}
Group:		Development/Python
Requires:	%{name} = %{version}

%description devel
Development files of the Gnome Python wrappers.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm {} \;

%files
%doc AUTHORS ChangeLog
%dir %{py_platsitedir}/gtk-2.0/mate/
%{py_platsitedir}/gtk-2.0/mate/__init__.*
%{py_platsitedir}/gtk-2.0/mate/_mate.so
%{py_platsitedir}/gtk-2.0/mate/ui.so

%files -n %{oname}-matecanvas
%doc examples/canvas
%{py_platsitedir}/gtk-2.0/mate/canvas.*
%{py_platsitedir}/gtk-2.0/matecanvas.so

%files -n %{oname}-matecomponent
%doc examples/matecomponent
%dir %{py_platsitedir}/gtk-2.0/matecomponent/
%{py_platsitedir}/gtk-2.0/matecomponent/__init__.*
%{py_platsitedir}/gtk-2.0/matecomponent/*.so

%files -n %{oname}-mateconf
%doc examples/mateconf
%{py_platsitedir}/gtk-2.0/mateconf*

%files -n %{oname}-matevfs
%doc examples/vfs
%{py_platsitedir}/gtk-2.0/mate/vfs*
%{py_platsitedir}/gtk-2.0/matevfs
%{_libdir}/mate-vfs-2.0/modules/libpythonmethod.so

%files devel
%{_includedir}/mate-python-2.0/pymatevfs.h
%{_includedir}/mate-python-2.0/pymatevfsmatecomponent.h
%doc %_datadir/gtk-doc/html/pymatevfs
%{_libdir}/pkgconfig/mate-python-2.0.pc
%dir %{_datadir}/pygtk/2.0/defs
%{_datadir}/pygtk/2.0/defs/*.defs
%{_datadir}/pygtk/2.0/defs/mate/*.defs
%{_datadir}/pygtk/2.0/argtypes



%changelog
* Tue Jun 12 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-3
+ Revision: 805271
- rebuild adding requires to make MATE function properly

* Fri Jun 08 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-2
+ Revision: 803243
- rebuild to remove extra mate in sub pkg names

* Tue Jun 05 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 802527
- imported package python-mate

