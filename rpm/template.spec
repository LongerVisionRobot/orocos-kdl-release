Name:           ros-lunar-orocos-kdl
Version:        1.3.1
Release:        0%{?dist}
Summary:        ROS orocos_kdl package

Group:          Development/Libraries
License:        LGPL
URL:            http://wiki.ros.org/orocos_kdl
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       pkgconfig
Requires:       ros-lunar-catkin
BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  eigen3-devel

%description
This package contains a recent version of the Kinematics and Dynamics Library
(KDL), distributed by the Orocos Project.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Tue Mar 28 2017 Ruben Smits <ruben@intermodalics.eu> - 1.3.1-0
- Autogenerated by Bloom

