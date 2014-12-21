Name:           ros-indigo-rosprofiler
Version:        0.1.2
Release:        0%{?dist}
Summary:        ROS rosprofiler package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/rosprofiler
Source0:        %{name}-%{version}.tar.gz

Requires:       python-psutil
Requires:       ros-indigo-ros-statistics-msgs
Requires:       ros-indigo-ros-topology-msgs
Requires:       ros-indigo-rosgraph
Requires:       ros-indigo-rosnode
Requires:       ros-indigo-rospy
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rospy-tutorials
BuildRequires:  ros-indigo-rostest

%description
The rosprofiler package provides the rosprofiler and rosgrapher tools. These
tools run as nodes publishing their collected information on ros topics. They
have been designed to work with the Topic Statistics feature found in ROS Indigo
to provide a complete picture of a ROS System.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Dec 21 2014 Dan Brooks <dan@osrfoundation.org> - 0.1.2-0
- Autogenerated by Bloom

