    &XC
      &XC_FUNCTIONAL  BEEFVDW
      &END XC_FUNCTIONAL
      &VDW_POTENTIAL
        &NON_LOCAL
            TYPE LMKLL
            KERNEL_FILE_NAME vdW_kernel_table.dat
        &END NON_LOCAL
      &END VDW_POTENTIAL
    &END XC
