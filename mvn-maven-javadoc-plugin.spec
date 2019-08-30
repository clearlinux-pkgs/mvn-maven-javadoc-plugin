#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-javadoc-plugin
Version  : 3.0.0.m1
Release  : 5
URL      : https://github.com/apache/maven-javadoc-plugin/archive/maven-javadoc-plugin-3.0.0-M1.tar.gz
Source0  : https://github.com/apache/maven-javadoc-plugin/archive/maven-javadoc-plugin-3.0.0-M1.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-javadoc-plugin/3.0.0-M1/maven-javadoc-plugin-3.0.0-M1.jar
Source2  : https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-javadoc-plugin/3.0.0-M1/maven-javadoc-plugin-3.0.0-M1.pom
Source3  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-javadoc-plugin/2.10.3/maven-javadoc-plugin-2.10.3.jar
Source4  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-javadoc-plugin/2.10.3/maven-javadoc-plugin-2.10.3.pom
Source5  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-javadoc-plugin/3.0.1/maven-javadoc-plugin-3.0.1.jar
Source6  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-javadoc-plugin/3.0.1/maven-javadoc-plugin-3.0.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-javadoc-plugin-data = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-javadoc-plugin package.
Group: Data

%description data
data components for the mvn-maven-javadoc-plugin package.


%prep
%setup -q -n maven-javadoc-plugin-maven-javadoc-plugin-3.0.0-M1

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-javadoc-plugin/3.0.0-M1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-javadoc-plugin/3.0.0-M1/maven-javadoc-plugin-3.0.0-M1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-javadoc-plugin/3.0.0-M1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-javadoc-plugin/3.0.0-M1/maven-javadoc-plugin-3.0.0-M1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-javadoc-plugin/2.10.3
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-javadoc-plugin/2.10.3/maven-javadoc-plugin-2.10.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-javadoc-plugin/2.10.3
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-javadoc-plugin/2.10.3/maven-javadoc-plugin-2.10.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-javadoc-plugin/3.0.1
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-javadoc-plugin/3.0.1/maven-javadoc-plugin-3.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-javadoc-plugin/3.0.1
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-javadoc-plugin/3.0.1/maven-javadoc-plugin-3.0.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-javadoc-plugin/2.10.3/maven-javadoc-plugin-2.10.3.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-javadoc-plugin/2.10.3/maven-javadoc-plugin-2.10.3.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-javadoc-plugin/3.0.0-M1/maven-javadoc-plugin-3.0.0-M1.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-javadoc-plugin/3.0.0-M1/maven-javadoc-plugin-3.0.0-M1.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-javadoc-plugin/3.0.1/maven-javadoc-plugin-3.0.1.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-javadoc-plugin/3.0.1/maven-javadoc-plugin-3.0.1.pom
