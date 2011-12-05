Name: srptools
Version: 0.0.4
Release: 8%{?dist}
Summary: Tools for using the InfiniBand SRP protocol devices
Group: System Environment/Base
License: GPLv2 or BSD
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/%{name}/%{name}-%{version}-0.1.gce1f64c.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libibumad-devel, libibverbs-devel >= 1.1.2-4
ExclusiveArch: i386 x86_64 ia64 ppc ppc64
Obsoletes: openib-srptools <= 0.0.6

%description
In conjunction with the kernel ib_srp driver, srptools allows you to
discover and use SCSI devices via the SCSI RDMA Protocol over InfiniBand.

%prep
%setup -q

%build
%configure
make CFLAGS="$CFLAGS -fno-strict-aliasing" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/srp_daemon.conf
%{_sbindir}/ibsrpdm
%{_sbindir}/srp_daemon
%{_sbindir}/srp_daemon.sh
%{_sbindir}/run_srp_daemon
%{_mandir}/man1/ibsrpdm.1*
%{_mandir}/man1/srp_daemon.1*
%doc README NEWS ChangeLog COPYING

%changelog
* Mon Jan 25 2010 Doug Ledford <dledford@redhat.com> - 0.0.4-8.el6
- Update to latest upstream version so we can have an actual URL that works
- Fix ups for pkgwrangler import and also fix bug reported against rhel5
  version of package (552915)
- Related: bz543948

* Tue Dec 22 2009 Doug Ledford <dledford@redhat.com> - 0.0.4-7.el5
- Bump and rebuild against new libibumad
- Related: bz518218

* Mon Jun 22 2009 Doug Ledford <dledford@redhat.com> - 0.0.4-6.el5
- Rebuild against libibverbs that isn't missing the proper ppc wmb() macro
- Related: bz506258

* Sun Jun 21 2009 Doug Ledford <dledford@redhat.com> - 0.0.4-5.el5
- Build against non-XRC libibverbs
- Update to ofed 1.4.1 final bits
- Related: bz506258, bz506097

* Fri Apr 24 2009 Doug Ledford <dledford@redhat.com> - 0.0.4-4.el5
- Add -fno-strict-aliasing to CFLAGS

* Sat Apr 18 2009 Doug Ledford <dledford@redhat.com> - 0.0.4-3.el5
- Bump and rebuild against updated libibverbs and libibumad
- Related: bz459652

* Tue Apr 01 2008 Doug Ledford <dledford@redhat.com> - 0.0.4-2
- Update to OFED 1.3 final bits
- Related: bz428197

* Tue Jan 29 2008 Doug Ledford <dledford@redhat.com> - 0.0.4-1
- Import upstream srptools and obsolete old openib-srptools package
- Related: bz428197

