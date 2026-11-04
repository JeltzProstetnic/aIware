


     /* D A T E N B O X Z E R L E G U N G  N A C H   W I T T M A N N    2 0 0 1*/

                              /*I */


            /* DATENBOX-ZERLEGUNG OHNE REPLIKATION*/

                           /*9.10.0I - erstellt von Dr.MUTZ*/


 /*Das Programm zerlegt nach Wittmann (1985) und Stemmler & Fahrenberg (1989) eine
   dreidimensionale Datenbox (Personen, Situation/Zeitpunkte, Variablen) ohne Replikation mit
   den folgenden Analyseelementen:
   1. Deskriptive Statistiken Person, Situation
   2. Erzeugen der Kreuzproduktmatrizen total, zwischen Personen (bp), zwischen Situationen (bs)
      Residual(res), innerhalb von Personen (wp), innerhalb von Situationen (ws)
   3. Korrelationsmatrix (total,bp,bs,wp,ws,res) normiert an der totalen Kovarianzmatrix
      ->Eta²-Koeffizienten, Anteile aufgeklaerter Streuung
   4. Korrelationsmatrix (total,bp,bs,wp,ws,res) normiert an der jeweiligen Kovarianzmatrix
      ->Korrelationskoeffizienten (bp, bs...) mit Signifikanztest (mit und ohne Greenhouse-
      Geiser-Korrektur) und calculated probability
   5. Koeffizienten der Multivariaten Reliabilitaets- und Generalisierbarkeitstheorie nach
      Wittmann
   6. Faktorenanalyse der Korrelationsmatrizen (total, bs, bp,wp,ws res), normiert an der
      jeweiligen Kovarianzmatrix->Dimensionen interindividueller und intraindivueller
      Veraenderung....

                    */

 /*Programm-Ablauf: 1. Dateneingabe in der Datenstrukur wie im Beispiel (s.u.) mit den
                       Variablen in den Spalten und der Identifikation der Person und des
                       Zeitpunktes.
                    2. Eingabe der Variablenname fuer die Identifikation der Person und des
                       Zeitpunkts und die Namen der benutzten Items in die Makrovariablen
                       PERSON, ZEITP und VARIAB. Eine Eingabe der Anzahl der Personen oder
                       Zeitpunkte ist nicht notwendig. ACHTUNG! MISSING VALUEs zeilenweise
                       vorher loeschen oder mit einem Filler ersetzen.
                    3. Durchlauf des Programms mit RUN*/


  /*Beispiel: p=9 Personen werden zu k=3 Zeitpunkten hinsichtlich j=6 verschiedenen Items
              wiederholt befragt.*/

   options ps=65 ls=70 pageno=1 nodate;

   /*libname reg 'C:\...';*/


 /**************************************************************************/
 /*             E I N L E S E N  D E R  D A T E N                          */
 /**************************************************************************/

data rohdat;
input pnr time item1 item2 item3 item4 item5 item6;
cards;
1 1 3.703 4.557 5.938 4.718 4.601  4.696
1 2 3.503 6.557 4.938 4.418 4.701  4.296
1 3 2.000 4.000 6.000 4.500 2.500  6.000
2 1 2.000 5.000 6.000 6.000 6.000  5.500
2 2 3.000 5.000 7.000 5.000 4.500  3.000
2 3 4.000 7.000 7.000 7.000 6.500  7.000
3 1 6.000 4.000 6.000 5.500 4.500  4.500
3 2 3.703 4.557 5.938 4.718 4.601  4.696
3 3 3.703 4.557 5.938 4.718 4.601  4.696
4 1 1.000 4.000 4.000 4.500 4.000  4.000
4 2 3.000 5.000 7.000 5.000 4.000  5.000
4 3 3.703 4.557 5.938 4.718 4.601  4.696
5 1 5.000 5.000 7.000 6.000 6.500  4.500
5 2 7.000 5.000 6.000 6.000 4.500  5.500
5 3 2.000 5.000 7.000 5.000 4.500  4.500
6 1 6.000 4.000 6.000 6.000 5.500  5.500
6 2 3.703 4.557 5.938 4.718 4.601  4.696
6 3 4.000 6.000 5.000 5.500 1.500  3.500
7 1 5.000 5.000 6.000 6.000 4.000  5.000
7 2 2.000 4.000 4.000 4.500 6.000  5.500
7 3 3.703 4.557 5.938 4.718 4.601  4.696
8 1 3.000 5.000 5.000 5.000 5.500  5.000
8 2 1.000 1.000 7.000 2.000 4.000  4.000
8 3 6.000 6.000 7.000 4.500 5.000  5.000
9 1 4.000 2.000 4.000 3.000 2.000  3.000
9 2 3.703 4.557 5.938 4.718 4.601  4.696
9 3 3.000 5.000 7.000 4.500 4.000  4.500
;
run;


 /********************************************************************************/
 /*   E I N G A B E  D E R  I N P U T V A R I A B L E N  D E S  P R O G R A M M S*/
 /********************************************************************************/


   %LET VARIAB = ITEM1 ITEM2 ITEM3 ITEM4 ITEM5 ITEM6 ;/*Namen der Items/Variablen */
   %LET PERSON=PNR;                                   /*Variable der Personenidentifikation*/
   %LET ZEITP=TIME;                                   /*Variable der Zeitpunkt/
                                                        Situationsidentifikation*/
   %LET DATEN=ROHDAT;                                 /*Zuweisung des Datensatzes*/








/***************************************************************/
/*                  H A U P T P R O G R A M M                  */
/***************************************************************/


   data basdat;
   set &DATEN;
   run;


   /* 1. Erstellung des SUMMENVEKTORS fuer jede Variable ueber alle
   Zeitpunkte, d.h. Aggregierung ueber alle Zeitpunkte fuer n=? Personen */

   proc summary data=basdat sum;
   var &VARIAB;
   class &PERSON;
   output out =sumdat1 sum(&VARIAB)
              = &VARIAB;
   run;

   data sfpers gsum;
   set sumdat1;
   if _type_= 1 then output sfpers;
   if _type_= 0 then output gsum;
   run;

   /* 2. Erstellung des SUMMENVEKTORS fuer jede Variable ueber alle
      Personen, d.h. Aggregierung ueber alle Personen bei k=? Zeitpunkte*/

   proc summary data= basdat sum;
   var &VARIAB;
   class &ZEITP;
   output out= sumdat2 sum(&VARIAB)
         = &VARIAB;
   run;

   data sfsitu;
   set sumdat2;
   if _type_= 1;
   drop _TYPE_ _FREQ_ ;
   run;


   /* 3. Erstellung der MITTELWERTSVEKTOREN fuer jede Variable
   ueber alle Zeitpunkte, d.h. Aggregierung ueber alle Zeipunkte */

   proc summary data= basdat mean;
   var &VARIAB;
   class &PERSON;
   output out = mdat1 mean(&VARIAB)
              = &VARIAB;
   run;

   data mfpers;
   set mdat1;
   if _type_ = 1;
   drop _TYPE_ _FREQ_ ;
   run;


   title1 'DATENBOXZERLEGUNG - OHNE REPLIKATION - MUTZ/2001            ';
   title2 '1. Vektoren der Mittelwerte der Variablen                   ';
   title3 '1.1. Mittelwert fuer jede Person ueber Zeitpunkte aggregiert';
   proc print data=mfpers width=minimum round;
   var &PERSON &VARIAB;
   run;

  /*4. Erstellung der MITTELWERTSVEKTOREN fuer jede Variable ueber
   alle Personen, d.h. Aggregierung ueber alle Zeitpunkte bei k= ?
   Zeitpunkte */

   proc summary data = basdat mean;
   var &VARIAB;
   class &ZEITP;
   output out = mdat2 mean(&VARIAB)
              = &VARIAB;
   run;

   data mfsitu;
   set mdat2;
   if _type_ = 1;
   drop _TYPE_ _FREQ_ ;
   run;


   title1 'DATENBOXZERLEGUNG - OHNE REPLIKATION - MUTZ/2001                    ';
   title2 '1. Vektoren der Mittelwerte der Variablen                           ';
   title3 '1.2. Mittelwert fuer jeden Zeitpunkte ueber alle Personen aggregiert';

   proc print data=mfsitu width=minimum round;
   var &ZEITP &VARIAB;
   run;







   /*5. MULTIVARIATE KREUZPRODUKTZERLEGUNG */
   proc iml;

   reset noprint;

   /* 5.1 Erstellung der Ausgangsmatrizen fuer die Berechnung der
      Kreuzprodukte und Korrelation */

   satz1 = {&VARIAB};
   satz2 = {&VARIAB};

   use sfpers;
   read all var satz1 into XFP;
   use sfsitu;
   read all var satz1 into XFS;
   use gsum;
   read all var satz1 into XG;
   use basdat;
   read all var satz2 into X;

   Ng = NROW(X);  /* Gesamtzahl der Beobachtungen*/
   Q  = NCOL(X);  /* Anzahl der Variablen */
   P  = NROW(XFP);/* Anzahl der Personen*/
   k  = NROW(XFS);/* Anzahl der Zeitpunkte*/

  /* Prozedur, die das Inverse der Wurzel von Diagonalelementen
     einer Matrix wiedergibt.*/

   START IN (G,A);
   A = DIAG(1/SQRT(VECDIAG(G)));
   FINISH;


  /* 5.2. Multivariate Kreuzproduktzerlegung*/
  /* Kreuzprodukte */

   SStot  = X` * X - XG ` * XG/Ng;
   SSbp   = XFP` * XFP * 1/k  - XG ` * XG /Ng;
   SSbs   = XFS` * XFS * 1/p  - XG ` * XG /Ng;
   SSres  = SStot - SSbp - SSbs;
   SSws   = SStot - SSbs;
   SSwp   = SStot - SSbp;


  /* Korrelationsmatrizen mit der Normierung an dem
    Totalvarianzvektor*/

   RUN IN (SStot, S);

   Rtot = S  * SStot * S;
   Rbp  = S  * SSbp  * S;
   Rbs  = S  * SSbs  * S;
   Rwp  = S  * SSwp  * S;
   Rws  = S  * SSws  * S;
   Rres = S  * SSres * S;

  /* Korrelationsmatrizen mit der Normierung an der jeweiligen
     Varianz der Kovarianzmatrix */

   RUN IN (SStot, S);
   Rtotc = S  * SStot * S;

   RUN IN (SSbp, SBP);
   Rbpc  = SBP * SSbp * SBP;

   RUN IN (SSbs, SBS);
   Rbsc  = SBS * SSbs * SBS;

   RUN IN (SSwp, SWP);
   Rwpc  = SWP * SSwp * SWP;

   RUN IN (SSws, SWS);
   Rwsc  = SWS  *SSws * SWS;

   RUN IN (SSres, SRES);
   Rresc = SRES * SSres * SRES;

   R_TEST=-2*k*p*log(abs(det(Rresc)));

   df=q*(q-1)/2;
   PROB_R=1-probchi(R_TEST,df);



   /* 5. T-Tests der Korrelationen der einzelnen Matrizen*/
   /* 5.3. ohne GREENHOUSE-GEISSER-Korrektur*/

   AI=SHAPE(1,q,q);
   AII=DIAG(AI);

   QR=(AI-Rtotc##2)+AII;
   Ttot=((Rtotc*(k*p-2)##0.5)/(QR##0.5))-q*AII;
   Ptot=AI-PROBT(ABS(Ttot),k*p-1);

   QR=(AI-Rbpc##2)+AII;
   Tbp=((Rbpc*(p-2)##0.5)/(QR##0.5))-q*AII;
   Pbp=AI-PROBT(ABS(Tbp),p-1);


   QR=ABS(AI-Rbsc##2)+AII;
   Tbs=((Rbsc*(k-2)##0.5)/(QR##0.5))-q*AII;
   Pbs=AI-PROBT(ABS(Tbs),k-1);

   QR=(AI-Rwpc##2)+AII;
   Twp=((Rwpc*(p*k-2)##0.5)/(QR##0.5))-q*AII;
   Pwp=AI-PROBT(ABS(Twp),p*(k-1));

   QR=(AI-Rwsc##2)+AII;
   Tws=((Rwsc*(k*p-2)##0.5)/(QR##0.5))-q*AII;
   Pws=AI-PROBT(ABS(Tws),k*(p-1));

   QR=(AI-Rresc##2)+AII;
   Tres=((Rresc* (k*p-2)##0.5)/(QR##0.5))-q*AII;
   Pres=AI-PROBT(ABS(Tres),(k-1)*(p-1));


    /*5.4. mit GREENHOUSE-GEISSER-Korrektur*/
   AI=SHAPE(1,q,q);
   AII=DIAG(AI);

   QR=(AI-Rtotc##2)+AII;
   Ttotg=((Rtotc*(2*p-2)##0.5)/(QR##0.5))-q*AII;
   Ptotg=AI-PROBT(ABS(Ttotg),2*p-1);

   QR=(AI-Rbpc##2)+AII;
   Tbpg=((Rbpc*(p-2)##0.5)/(QR##0.5))-q*AII;
   Pbpg=AI-PROBT(ABS(Tbpg),p-1);


   QR=ABS(AI-Rbsc##2)+AII;
   Tbsg=(Rbsc/(QR##0.5))-q*AII;
   Pbsg=AI-PROBT(ABS(Tbsg),k-1);

   QR=(AI-Rwpc##2)+AII;
   Twpg=((Rwpc*(p-2)##0.5)/(QR##0.5))-q*AII;
   Pwpg=AI-PROBT(ABS(Twpg),p);

   QR=(AI-Rwsc##2)+AII;
   Twsg=((Rwsc*(2*p-2)##0.5)/(QR##0.5))-q*AII;
   Pwsg=AI-PROBT(ABS(Twsg),2*(p-1));

   QR=(AI-Rresc##2)+AII;
   Tresg=((Rresc*(p-2)##0.5)/(QR##0.5))-q*AII;
   Presg=AI-PROBT(ABS(Tresg),p-1);
   free QR AI AII;

 /* 6. Multivariate Reliabilitaetskoeffizienten*/

  /*6.1. Multivariater Reliabilitaetskoeffizient-Summenskala*/

    RTTbp = SSbp[+,+]/SStot[+,+];
    RTTbs = SSbs[+,+]/SStot[+,+];
    RTTres= SSres[+,+]/SStot[+,+];
    RTTtot= RTTbp+RTTbs;


 /*6.2. Multivariater Reliabilitaetskoeffizient-multivariate
            Spurenkorrelation*/

    Etot = eigvec(SStot);
    Ltot = diag(Etot`*SStot*Etot);
    Lbp  = diag(Etot`*SSbp *Etot);
    Lbs  = diag(Etot`*SSbs *Etot);
    Lres = diag(Etot`*SSres*Etot);
    Ltrue= diag(Etot`*(SSbp+SSbs)*Etot);


    TTbp =sum(vecdiag(Lbp)  /vecdiag(Ltot))/q;
    TTbs =sum(vecdiag(Lbs)  /vecdiag(Ltot))/q;
    TTres=sum(vecdiag(Lres) /vecdiag(Ltot))/q;
    TTtot=sum(vecdiag(Ltrue)/vecdiag(Ltot))/q;


  /*6.3. Multivariater Reliabilitaetskoeffizient-maximierte
             Reliabilitaet*/

    Etot = eigvec(SStot);
    Etot = Etot[,1];/*Erstellung des Gewichtsvektor = groesster
                      Eigenvektor*/

    Ltot = diag(Etot`*SStot*Etot);
    Lbp  = diag(Etot`*SSbp *Etot);
    Lbs  = diag(Etot`*SSbs *Etot);
    Lres = diag(Etot`*SSres*Etot);
    Ltrue= diag(Etot`*(SSbp+SSbs)*Etot);


    RMAXbp =sum(vecdiag(Lbp)  /vecdiag(Ltot));
    RMAXbs =sum(vecdiag(Lbs)  /vecdiag(Ltot));
    RMAXres=sum(vecdiag(Lres) /vecdiag(Ltot));
    RMAXtot=sum(vecdiag(Ltrue)/vecdiag(Ltot));


  /*6.. Generalisierbarkeitstheorie*/

    Ubp =SSbp [+,+]/(SSbp [+,+]  + SSres[+,+]);
    Ubs =SSbs [+,+]/(SSbs [+,+]  + SSres[+,+]);


    /* 7. AUSDRUCK DER ERGEBNISSE DER MULTIVARIATE KOVARIANZZERLEGUNG
    */



   title1 'DATENBOXZERLEGUNG - OHNE REPLIKATION - MUTZ/2001';
   title2 '2. Ergebnisse der Datenboxzerlegung             ';
   title3 'Kovarianz-, Korrelationsmatrizen, Signifik.     ';
   title4;

   print " Zahl der Variablen: ",, Q;
   print " Zahl der Personen: ",, P;
   print " Zahl der Zeitpunkte: ",,K;
   print " Gesamtzahl der Beobachtungen: ",,Ng;


   print "2.1. CROSS-PRODUCT-PARTITIONING";
   print "CROSS-PRODUCTS: TOTAL"              ,, SStot [r=satz2 c=satz2 ];
   print "CROSS-PRODUCTS: BETWEEN PERSONS"      ,, SSbp  [r=satz2 c=satz2 ];
   print "CROSS-PRODUCTS: BETWEEN SITUATIONS",, SSbs  [r=satz2 c=satz2 ];
   print "CROSS-PRODUCTS: WITHIN PERSONS "      ,, SSwp  [r=satz2 c=satz2 ];
   print "CROSS-PRODUCTS: WITHIN SITUATIONS" ,, SSws  [r=satz2 c=satz2 ];
   print "CROSS-PRODUCTS: RESIDUAL"           ,, SSres [r=satz2 c=satz2 ];

   print "2.2. CORRELATIONSMATRIX - NORMIERUNG AN DER TOTALMATRIX";
   print "CORRELATION-MATRIX: TOTAL",,                Rtot [r=satz2 c=satz2];
   print "CORRELATION-MATRIX: BETWEEN PERSONS",,      Rbp  [r=satz2 c=satz2];
   print "CORRELATION-MATRIX: BETWEEN SITUATIONS",,   Rbs  [r=satz2 c=satz2];
   print "CORRELATION-MATRIX: WITHIN PERSONS",,       Rwp  [r=satz2 c=satz2];
   print "CORRELATION-MATRIX: WITHIN SITUATIONS",,    Rws  [r=satz2 c=satz2];
   print "CORRELATION-MATRIX: RESIDUAL",,             Rres [r=satz2 c=satz2];


   print "2.3. CORRELATIONS-MATRIX - NORMIERT AN EINZELNER KOVARIANZMATRIX";
   print "CORRELATION-MATRIX: TOTAL",,                Rtotc [r=satz2 c=satz2];
   print "CORRELATION-MATRIX: BETWEEN PERSONS",,      Rbpc  [r=satz2 c=satz2];
   print "CORRELATION-MATRIX: BETWEEN SITUATIONS",,   Rbsc  [r=satz2 c=satz2];
   print "CORRELATION-MATRIX: WITHIN PERSONS",,       Rwpc  [r=satz2 c=satz2];
   print "CORRELATION-MATRIX: WITHIN SITUATIONS",,    Rwsc  [r=satz2 c=satz2];
   print "CORRELATION-MATRIX: RESIDUAL",,             Rresc [r=satz2 c=satz2];

   print "2.4. T-TESTS DER KORRELATIONEN - NORMIERT AN EINZELNER KOVARIANZMATRIX";
   print "2.4.1. T-TESTS OHNE GREENHOUSE-GEISSER-KORREKTUR";
   print "T-TEST VON Rtot MIT SIGNIFIKANZ: ",,Ttot [r=satz2 c=satz2],
                                              Ptot [r=satz2 c=satz2];
   print "T-TEST VON Rbp  MIT SIGNIFIKANZ: ",,Tbp [r=satz2 c=satz2],
                                              Pbp [r=satz2 c=satz2];
   print "T-TEST VON Rbd  MIT SIGNIFIKANZ: ",,Tbs [r=satz2 c=satz2],
                                              Pbs [r=satz2 c=satz2];
   print "T-TEST VON Rwp  MIT SIGNIFIKANZ: ",,Twp [r=satz2 c=satz2],
                                              Pwp [r=satz2 c=satz2];
   print "T-TEST VON Rws  MIT SIGNIFIKANZ: ",,Tws [r=satz2 c=satz2],
                                              Pws [r=satz2 c=satz2];
   print "T-TEST VON Rres MIT SIGNIFIKANZ: ",,Tres [r=satz2 c=satz2],
                                              Pres [r=satz2 c=satz2];

   print "2.4. T-TESTS DER KORRELATIONEN - NORMIERT AN EINZELNER KOVARIANZMATRIX";
   print "2.4.2. T-TESTS MIT GREENHOUSE-GEISSER-KORREKTUR";
   print "T-TEST VON Rtot MIT SIGNIFIKANZ: ",,Ttotg [r=satz2 c=satz2],
                                              Ptotg [r=satz2 c=satz2];
   print "T-TEST VON Rbp  MIT SIGNIFIKANZ: ",,Tbpg [r=satz2 c=satz2],
                                              Pbpg [r=satz2 c=satz2];
   print "T-TEST VON Rbs  MIT SIGNIFIKANZ: ",,Tbsg [r=satz2 c=satz2],
                                              Pbsg [r=satz2 c=satz2];
   print "T-TEST VON Rwp  MIT SIGNIFIKANZ: ",,Twpg [r=satz2 c=satz2],
                                              Pwpg [r=satz2 c=satz2];
   print "T-TEST VON Rws  MIT SIGNIFIKANZ: ",,Twsg [r=satz2 c=satz2],
                                              Pwsg [r=satz2 c=satz2];
   print "T-TEST VON Rres MIT SIGNIFIKANZ: ",,Tresg [r=satz2 c=satz2],
                                              Presg [r=satz2 c=satz2];


   print "PRUEFUNG: H0: RESIDUALMATRIX=IDENTITAETSMATRIX";
   print "CHI2-Wert=" R_TEST "df=" df "p=" PROB_R;



    print "2.5. MULTIVARIATE RELIABILITAETSTHEORIE                ";
    print "                                                       ";
    print "2.5.1. Multivariate Reliabilitaet-Summenskala(RTT)";
    print "Multivariate Reliabilitaet - zwischen Personen         ",,Rttbp;
    print "Multivariate Reliabilitaet - zwischen Situationen      ",,Rttbs;
    print "Multivariate Reliabilitaet - Residual/Interaktion      ",,Rttres;
    print "Multivariate Reliabilitaet - TOTAL(BP, BS)             ",,Rtttot;

    print "                                                       ";
    print "2.5.2. Multivariate Reliabilitaet-Spurenkorrelation(TT)";
    print "Multivariate Reliabilitaet - zwischen Personen         ",,TTbp;
    print "Multivariate Reliabilitaet - zwischen Situationen      ",,TTbs;
    print "Multivariate Reliabilitaet - Residual/Interaktion      ",,TTres;
    print "Multivariate Reliabilitaet - TOTAL(BP, BS)             ",,TTtot;


    print "                                                       ";
    print "2.5.3. Multivariate Reliabilitaet-Maximierte Reliabilitaet(RMAX)";
    print "Multivariate Reliabilitaet - zwischen Personen         ",,RMAXbp;
    print "Multivariate Reliabilitaet - zwischen Situationen      ",,RMAXbs;
    print "Multivariate Reliabilitaet - Residual/Interaktion      ",,RMAXres;
    print "Multivariate Reliabilitaet - TOTAL(BP, BS)             ",,RMAXtot;

    print "2.6. MULTIVARIATE GENERALISIERBARKEITSTHEORIE          ";
    print "                                                       ";
    print "Multivariate Generalisierbarkeit - zwischen Personen   ",,Ubp;
    print "Multivariate Generalisierbarkeit - zwischen Situationn ",,Ubs;


    free Ttotg Ptotg Tbpg Pbpg Tbsg Pbsg Twpg Pwpg Twsg Pwsg Tresg Presg
         Ttot Ptot Tbp Pbp Tbs Pbs Twp Pwp Tws Pws Tres Pres;


   quit;






   /* 8. OUTPUT DER MATRIZEN UND DATENTRANSFORMATION*/
   /* 8.1. Erstellung der Ausgangsmatrizen fuer die Berechnung der
           Kreuzprodukte und Korrelation */

   proc iml;

   reset noprint;


   use sfpers;
   satz1 = { &VARIAB };
   satz2 = { &VARIAB };
   read all var satz1 into XFP;
   use sfsitu;
   read all var satz1 into XFS;
   use gsum;
   read all var satz1 into XG;
   use basdat;
   read all var satz2 into X;

   Ng = NROW(X);  /* Gesamtzahl der Beobachtungen*/
   Q  = NCOL(X);  /* Anzahl der Variablen */
   P  = NROW(XFP);/* Anzahl der Personen*/
   k  = NROW(XFS); /* Anzahl der Zeitpunkte*/

   /* Prozedur, die das Inverse der Wurzel von Diagonalelementen
      einer Matrix wiedergibt.*/

   START IN (G,A);
   A = DIAG(1/SQRT(VECDIAG(G)));
   FINISH;


   /* 8.2. Multivariate Kreuzproduktzerlegung*/
   /* Kreuzprodukte */

   SStot  = X` * X - XG ` * XG/Ng;
   SSbp   = XFP` * XFP * 1/k  - XG ` * XG /Ng;
   SSbs   = XFS` * XFS * 1/p  - XG ` * XG /Ng;
   SSres  = SStot - SSbp - SSbs;
   SSws   = SStot - SSbs;
   SSwp   = SStot - SSbs;

   /* Korrelationsmatrizen mit der Normierung an dem
      Totalvarianzvektor*/

   RUN IN (SStot, S);

   Rtot = S  * SStot * S;
   Rbp  = S  * SSbp  * S;
   Rbs  = S  * SSbs  * S;
   Rwp  = S  * SSwp  * S;
   Rws  = S  * SSws  * S;
   Rres = S  * SSres * S;

   /* Korrelationsmatrizen mit der Normierung an der jeweiligen
      Varianz der Kovarianzmatrix */

   RUN IN (SStot, S);
   Rtotc = S  * SStot * S;

   RUN IN (SSbp, SBP);
   Rbpc  = SBP * SSbp * SBP;

   RUN IN (SSbs, SBS);
   Rbsc  = SBS * SSbs * SBS;

   RUN IN (SSwp, SWP);
   Rwpc  = SWP * SSwp * SWP;

   RUN IN (SSws, SWS);
   Rwsc  = SWS  *SSws * SWS;

   RUN IN (SSres, SRES);
   Rresc = SRES * SSres * SRES;

 /*8.3. Erzeugung von SAS-Datensaetzen */

   varmat=satz1`;

   VARNAME = {&VARIAB};
   create CORtotc from Rtotc [COLNAME = VARNAME];
   append from Rtotc; free Rtotc;
   create CORbpc from Rbpc   [COLNAME = VARNAME];
   append from Rbpc;free Rbpc;
   create CORbsc  from Rbsc  [COLNAME = VARNAME];
   append from Rbsc;free Rbsc;
   create CORwpc  from Rwpc  [COLNAME = VARNAME];
   append from Rwpc;free Rwpc;
   create CORwsc  from Rwsc  [COLNAME = VARNAME];
   append from Rwsc;free Rwsc;
   create CORresc from Rresc [COLNAME = VARNAME];
   append from Rresc;free Rresc;
   create x from varmat [COLNAME={NAME}];
   append from varmat;free varmat;

   X=Rtot+(I(q)-DIAG(Rtot));
   free Rtot; Rtot = X; free X;
   create CORtot from Rtot  [COLNAME = VARNAME];
   append from Rtot;
   X=Rbp+(I(q)-DIAG(Rbp));
   free Rbp; Rbp = X; free X;
   create CORbp  from Rbp   [COLNAME = VARNAME];
   append from Rbp;
   X=Rbs+(I(q)-DIAG(Rbs));
   free Rbs; Rbs = X; free X;
   create CORbs  from Rbs   [COLNAME = VARNAME];
   append from Rbs;
   X=Rwp+(I(q)-DIAG(Rwp));
   free Rwp; Rwp = X; free X;
   create CORwp  from Rwp   [COLNAME = VARNAME];
   append from Rwp;
   X=Rws+(I(q)-DIAG(Rws));
   free Rws; Rws = X; free X;
   create CORws  from Rws   [COLNAME = VARNAME];
   append from Rws;
   X=Rres+(I(q)-DIAG(Rres));
   free Rres; Rres = X; free X;
   create CORres from Rres  [COLNAME = VARNAME];
   append from Rres;
   quit;




   data dtotc (type = corr);
   merge x CORtotc;
   rename NAME=_NAME_;
   _type_ = "CORR";
   run;

   data dbpc (type = corr);
   merge x CORbpc;
   rename NAME=_NAME_;
   _type_ = "CORR";
   run;

   data dbsc (type = corr);
   merge x CORbsc;
   rename NAME=_NAME_;
   _type_ = "CORR";
   run;

   data dwpc (type = corr);
   merge x CORwpc;
   rename NAME=_NAME_;
   _type_ = "CORR";
   run;

   data dwsc (type = corr);
   merge x CORwsc;
   rename NAME=_NAME_;
   _type_ = "CORR";
   run;

   data dresc (type = corr);
   merge x CORresc;
    rename NAME=_NAME_;
   _type_ = "CORR";
   run;




 /* 9. DURCHFUEHRUNG VON FAKTORENANALYSEN FUER DIE EINZELNEN
       KORRELATIONSMATRIZEN */



   title1 'DATENBOXZERLEGUNG - OHNE REPLIKATION - MUTZ/2001              ';
   title2 '3. Faktorisierung der einzelnen Korrelationsmatrix            ';
   title3 'NORMIERT AN DER EINZELNEN KOVARIANZMATRIX                     ';
   title4 '3.1. Faktorenanalyse der totalen Korrelationsmatrix Rtot-total';
   proc factor data = dtotc rotate = varimax scree;
   run;
   title4 '3.2. Faktorenanalyse der Korrelationsmatrix Rbt-zw.Personen   ';
   proc factor data = dbpc rotate = varimax scree;
   run;
   title4 '3.3. Faktorenanalyse der Korrelationsmatrix Rbs-zw.Situation  ';
   proc factor data = dbsc rotate = varimax scree;
   run;
   title4 '3.4. Faktorenanalyse der Korrelationsmatrix Rwt-In.Person     ';
   proc factor data = dwpc rotate = varimax scree ;
   run;
   title4 '3.5. Faktorenanalyse der Korrelationsmatrix Rws-In.Situation  ';
   proc factor data = dwsc rotate = varimax  scree ;
   run;
   title4 '3.6. Faktorenanalyse der Korrelationsmatrix Rres-Residual     ';
   proc factor data = dresc rotate = varimax scree;
   run;
