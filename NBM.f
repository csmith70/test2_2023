       PROGRAM  MeanVariance
      IMPLICIT   NONE
      INTEGER :: Number, IOstatus, rdopst, rdst, i, a,sum2
      INTEGER :: icount,i2,npts,i1
      REAL    :: Data, Sum, num7, n, y,diff, diff2!line, varb, b
      REAL    :: Mean, Var, Std, sum34, avg, SumSQR, var2 
      REAL    :: stdev, total, num2, num3, num4, num5, num6
      character(30) :: rdfile, line5
      character(72) :: line, line2
      !parameter (narray_max=1000000)
      !real iarray_in(narray_max),iarray_out(narray_max)
      TYPE :: wx
          Character(5):: letter
          !real :: num
          !real :: num2
          !real :: num3
          !real:: num4
          !real :: num5
          !real :: num6
          
      END Type wx
      type(wx),dimension(1)::wxrep

      TYPE :: wx2
          real :: num
          !real :: num2
          !real :: num2
          !real :: num3
          !real :: num4
          !real :: num5
          !real :: num6
      END Type wx2
      type(wx2),dimension(1)::wxrep2
      

      open(unit=12, file='NBM.csv' , status='old',
     +access ='sequential',form='formatted')
      !do
      !write(*,'(a)', advance="no") "Input File Name: "
      !read (*,*) rdfile
      !open(12, file=rdfile, status="old", 
      !+action="read", position="rewind")
      !if (rdopst==0) exit
      !end do
      
      read(12,11)line
   11 FORMAT(A)
      write(*,*)line
      read(12,11)line2
      write(*,*)line2
              !icount=1
      !100 continue
      !read(1,*,end=102)i1,i2
      !iarray_in(icount)=i2
      !icount=icount+1
      !goto 100

      !102 continue        
      !npts=icount-1
      
      i = 1
      sum=0
      sum2=0
      do 
      read(12,*,iostat=rdst)wxrep, num2,num3,num4,num5,num6,num7
      !write(*,*)wxrep
      !write(*,*)num2,num3,num4,num5,num6,num7
      !write(*,*)num2
      if (rdst >0) stop "read error"
      if (rdst <0) exit
      if (MOD(i,2).eq.0) then
      sum = sum+num2+num3+num4+num5+num6+num7
      write(*,*)sum
      end if
      if (MOD(i,2).eq.1) then
      sum2 = sum2+num2+num3+num4+num5+num6+num7
      write(*,*)sum2
      end if
      diff = (sum-sum2)/(i/2)
      !write(*,*)diff
      !write(*,*)num3
      i = i+1
      end do
      diff2 = 0-diff
      write(*,*)'NBMv4.0 predicts temperatures that are',diff2,
     +'degrees warm.'
      close(12)
      !write(*,*)diff
      !diff = (sum-sum2)/2
      !write(*,*)diff
      END 
