Name: roboro-better-calllog 

# >> macros
BuildArch: noarch
# << macros

Summary: roboro-better-calllog
Version: 0.1
Release: 1
Group: Qt/Qt
License: TODO
URL: http://example.org/
Source0: %{name}-%{version}.tar.bz2
Source100: roboro-better-calllog.yaml
Requires: patchmanager

%description
The roboro-better-calllog contains a patch to
the voicecall-ui included on the Jolla to fix
the problem where numbers were not shown for contact names
in the calllog and in the dialer.
This patch is intended to be used with patchmanager.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/share/patchmanager/patches/
mv src/roboro-better-calllog %{buildroot}/usr/share/patchmanager/patches/
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches
# >> files
# << files 
