      &XC
         &VDW_POTENTIAL
            DISPERSION_FUNCTIONAL PAIR_POTENTIAL
            &PAIR_POTENTIAL
            !  CALCULATE_C9_TERM .TRUE.
               PARAMETER_FILE_NAME dftd3.dat
               REFERENCE_FUNCTIONAL PBE
               R_CUTOFF 15
               TYPE DFTD3
            &END PAIR_POTENTIAL
         &END VDW_POTENTIAL
         &XC_FUNCTIONAL PBE
         &END XC_FUNCTIONAL
      &END XC
