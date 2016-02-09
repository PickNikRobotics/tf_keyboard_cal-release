Name:           ros-jade-tf-keyboard-cal
Version:        0.1.0
Release:        0%{?dist}
Summary:        ROS tf_keyboard_cal package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/davetcoleman/tf_keyboard_cal
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-keyboard
Requires:       ros-jade-roscpp
Requires:       ros-jade-rosparam-shortcuts
Requires:       ros-jade-tf
Requires:       ros-jade-tf2
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-keyboard
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-roslib
BuildRequires:  ros-jade-rosparam-shortcuts
BuildRequires:  ros-jade-tf
BuildRequires:  ros-jade-tf2

%description
Allows manual control of a TF through the keyboard

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Feb 09 2016 Dave Coleman <davetcoleman@gmail.com> - 0.1.0-0
- Autogenerated by Bloom

* Mon Jan 04 2016 Dave Coleman <davetcoleman@gmail.com> - 0.0.5-0
- Autogenerated by Bloom

* Sat Dec 05 2015 Dave Coleman <davetcoleman@gmail.com> - 0.0.4-0
- Autogenerated by Bloom

* Sat Dec 05 2015 Dave Coleman <davetcoleman@gmail.com> - 0.0.3-0
- Autogenerated by Bloom

