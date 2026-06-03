

     /* D A T E N B O X Z E R L E G U N G  N A C H   W I T T M A N N   2 0 0 1*/

                              /*II */


            /* DATENBOX-ZERLEGUNG M I T REPLIKATION*/

                           /*9.10.0I erstellt von Dr.Mutz*/


 /*Das Programm zerlegt nach Wittmann (1985) und Stemmler & Fahrenberg (1989) eine
   dreidimensionale Datenbox (Personen, Situation/Zeitpunkte, Variablen) mit Replikation mit
   den folgenden Analyseelementen:
   1. Pruefung der Paralleltestqualitaet der Skalen
   2. Deskriptive Statistiken Person, Situation
   3. Kreuzproduktmatrizen fuer die verschiedenen Komponenten (total, bp,bs ...)
   4. Korrelationsmatrizen (total,bp,bs,pxs,wp,ws,res) normiert an der totalen Kovarianzmatrix
      ->Eta²-Koeffizienten, Anteile aufgeklaerter Streuung in der Diagonalen
   5. Korrelationsmatrix (total,bp,bs,pxs,wp,ws,res) normiert an der jeweiligen Kovarianzmatrix
      ->Korrelationskoeffizienten (bp, bs...) mit Signifikanztest (mit und ohne Greenhouse-
      Geiser-Korrektur) und calculated probability
   6. Koeffizienten der Multivariaten Reliabilitaets- und Generalisierbarkeitstheorie nach
      Wittmann
   7. Faktorenanalyse der Korrelationsmatrizen (total,bs,bp,pxs, res), normiert an der
      jeweiligen Kovarianzmatrix->Dimensionen interindiviudeller und intraindivueller
      Veraenderung...
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


 /*Beispiel: p=10 Personen(PNR) werden zu k=4 Messzeitpunkten(TIME) in j=2 Paralleltests(TEST)
             mit je q=6 parallelen Items/Skalen (ITEM1-ITEM6) getestet*/


   options ps=60 ls=70 pageno=1 nodate;

  /* libname reg 'C::...*/



 /**************************************************************************/
 /*            E I N L E S E N  D E S  D A T E N                           */
 /**************************************************************************/

 data rohdat;
 input pnr time test item1 item2 item3 item4 item5 item6;
 cards;
 1     1     1  3.95  3.33  3.08  4.03  3.61  3.67
 2     1     1  7.00  1.00  4.00  1.00  3.00  2.50
 3     1     1  5.00  4.00  5.00  2.00  2.67  3.00
 4     1     1  7.00  4.00  6.00  5.00  1.33  5.00
 5     1     1  3.95  3.33  3.08  4.03  3.61  3.67
 6     1     1  3.95  3.33  3.08  4.03  3.61  3.67
 7     1     1  7.00  5.00  6.00  6.00  4.00  6.50
 8     1     1  3.95  3.33  3.08  4.03  3.61  3.67
 9     1     1  3.95  3.33  3.08  4.03  3.61  3.67
10     1     1  6.00  2.00  3.00  3.00  3.33  1.50
 1     2     1  3.00  2.00  2.00  1.00  3.67  3.67
 2     2     1  2.00  1.00  1.00  1.00  4.00  3.50
 3     2     1  3.95  3.33  3.08  4.03  3.61  3.67
 4     2     1  3.95  3.33  3.08  4.03  3.61  3.67
 5     2     1  2.00  4.00  4.00  1.00  4.33  2.50
 6     2     1  2.00  1.00  3.00  1.00  2.00  2.00
 7     2     1  3.95  3.33  3.08  4.03  3.61  3.67
 8     2     1  6.00  5.00  6.00  7.00  6.00  3.50
 9     2     1  7.00  6.00  3.00  1.00  3.33  6.00
10     2     1  4.00  4.00  3.00  1.00  3.33  5.00
 1     3     1  4.00  1.00  1.00  1.00  3.33  2.00
 2     3     1  7.00  7.00  4.00  7.00  5.00  5.50
 3     3     1  6.00  3.00  3.00  5.00  5.00  2.50
 4     3     1  2.00  4.00  5.00  4.00  2.67  2.00
 5     3     1  7.00  7.00  4.00  4.00  7.00  5.00
 6     3     1  3.00  5.00  4.00  6.00  5.33  6.50
 7     3     1  4.00  1.00  2.00  5.00  3.67  2.00
 8     3     1  1.00  4.00  4.00  6.00  4.33  3.50
 9     3     1  4.00  3.00  1.00  6.00  3.00  1.50
10     3     1  6.00  5.00  5.00  4.00  5.00  5.00
 1     4     1  3.95  3.33  3.08  4.03  3.61  3.67
 2     4     1  1.00  4.00  4.00  6.00  4.00  3.67
 3     4     1  1.00  1.00  1.00  1.00  3.00  3.67
 4     4     1  3.95  3.33  3.08  4.03  3.61  3.67
 5     4     1  3.95  3.33  3.08  4.03  3.61  3.67
 6     4     1  1.00  1.00  1.00  1.00  3.00  3.67
 7     4     1  3.00  2.00  2.00  4.00  3.67  3.67
 8     4     1  6.00  5.00  4.00  6.00  6.00  3.67
 9     4     1  3.95  3.33  3.08  4.03  3.61  3.67
10     4     1  3.95  3.33  3.08  4.03  3.61  3.67
 1     1     2  4.31  3.43  4.18  3.45  3.53  3.23
 2     1     2  7.00  7.00  7.00  1.00  3.53  2.50
 3     1     2  5.00  3.00  6.00  2.00  3.33  4.00
 4     1     2  7.00  4.00  2.00  1.00  3.53  5.00
 5     1     2  4.31  3.43  4.18  3.45  3.53  3.23
 6     1     2  4.31  3.43  4.18  3.45  3.53  3.23
 7     1     2  6.00  6.00  7.00  4.00  3.53  6.00
 8     1     2  4.31  3.43  4.18  3.45  3.53  3.23
 9     1     2  4.31  3.43  4.18  3.45  3.53  3.23
10     1     2  1.00  1.00  4.00  2.00  3.53  2.00
 1     2     2  5.00  1.00  4.00  2.00  3.53  4.50
 2     2     2  3.00  7.00  4.18  1.00  4.00  2.50
 3     2     2  4.31  3.43  4.18  3.45  3.53  3.23
 4     2     2  4.31  3.43  4.18  3.45  3.53  3.23
 5     2     2  4.00  5.00  4.00  4.00  3.00  4.00
 6     2     2  1.00  5.00  3.00  4.00  1.00  1.00
 7     2     2  4.31  3.43  4.18  3.45  3.53  3.23
 8     2     2  6.00  7.00  6.00  6.00  3.53  5.00
 9     2     2  7.00  5.00  6.00  3.45  3.53  5.00
10     2     2  4.00  2.00  5.00  1.00  3.53  3.50
 1     3     2  4.00  1.00  1.00  1.00  2.33  1.50
 2     3     2  7.00  7.00  7.00  1.00  6.00  6.00
 3     3     2  4.00  3.00  4.00  2.00  3.00  3.00
 4     3     2  7.00  6.00  3.00  1.00  2.33  2.00
 5     3     2  7.00  6.00  5.00  3.00  5.00  5.00
 6     3     2  5.00  5.00  6.00  4.00  3.67  3.50
 7     3     2  5.00  2.00  2.00  4.00  3.33  1.50
 8     3     2  2.00  4.00  7.00  4.00  5.67  2.50
 9     3     2  6.00  2.00  1.00  3.00  3.53  3.00
10     3     2  5.00  4.00  6.00  3.00  4.33  4.50
 1     4     2  4.31  3.43  4.18  3.45  3.53  3.23
 2     4     2  2.00  1.00  4.00  4.00  3.00  2.00
 3     4     2  1.00  1.00  2.00  2.00  2.33  4.00
 4     4     2  4.31  3.43  4.18  3.45  3.53  3.23
 5     4     2  4.31  3.43  4.18  3.45  3.53  3.23
 6     4     2  1.00  1.00  4.00  1.00  2.00  1.00
 7     4     2  4.00  2.00  3.00  5.00  4.00  2.50
 8     4     2  6.00  6.00  5.00  4.00  5.33  4.50
 9     4     2  4.31  3.43  4.18  3.45  3.53  3.23
10     4     2  4.31  3.43  4.18  3.45  3.53  3.23
 ;
run;



 /********************************************************************************/
 /*   E I N G A B E  D E R  I N P U T V A R I A B L E N  D E S  P R O G R A M M S*/
 /********************************************************************************/


 %LET VARIAB=ITEM1 ITEM2 ITEM3 ITEM4 ITEM5 ITEM6;  /*Skalen des zwei Paralletests*/
 %LET TEST=TEST;                                   /*Identifikation der Testhaelfte*/
 %LET ZEITP=TIME;                                  /*Identifikation der Zeitpunkte/Situationen*/
 %LET PERSON=PNR;                                  /*Identifikation der Personen*/
 %LET DATEN =ROHDAT;                               /*Benennung des Datensatzes*/


 /*********************************************************************************/
 /*                         H A U P T P R O G R A M M                             */
 /*********************************************************************************/

  %LET VARITEM=%SCAN(&VARIAB,1);

    data basdat;
    set &DATEN;
    run;

 /*1. VORANALYSEN: PRUEFUNG DER PARALLELTESTQUALITAET*/

    data basdat;
    set basdat;
    summe=sum(of &VARIAB);
    run;

    data skaldat1;
    set basdat;
    if &TEST=1;
    score1=summe;
    run;

    data skaldat2;
    set basdat;
    if &TEST=2;
    score2=summe;
    run;


   title1 'DATENBOXZERLEGUNG - MIT REPLIKATION - MUTZ/2001              ';
   title2 '1. Voranalysen: Ueberpruefung der Paralleltestqualitaet    ';
   title3 '1.1. Mittelwerte der Summenscores pro Zeitpunkt/Testhaelfte';

   proc summary data=basdat;
   class &ZEITP &TEST;
   var summe;
   output out=meandat  n(summe)=N mean(summe)=M std(summe)=STD min(summe)=MIN max(summe)=MAX;
   run;


   data totdat zeitdat;
   set meandat;
   if _TYPE_=0 then output totdat;
   if _TYPE_=3 then output zeitdat;
   run;
   data meandat;
   set zeitdat totdat;
   drop _FREQ_ _TYPE_;
   run;

   proc print data=meandat noobs;
   run;


   proc sort data=skaldat1;by &ZEITP;
   proc corr data=skaldat1 noprint nocorr alpha out=corrdat1;
   var &VARIAB;
   by &ZEITP;
   run;


   data corrdat1;
   set corrdat1;
   if _TYPE_='RAWALPHA';
   rtt1=&VARITEM;
   drop _TYPE_ _NAME_ &VARIAB;
   run;

   proc corr data=skaldat2 noprint nocorr alpha out=corrdat2;
   var &VARIAB;
   by &ZEITP;
   run;

   data corrdat2;
   set corrdat2;
   if _TYPE_='RAWALPHA';
   rtt2=&VARITEM;
   drop _TYPE_ _NAME_ &VARIAB;
   run;

   proc sort data=skaldat1;by &PERSON &ZEITP;
   proc sort data=skaldat2;by &PERSON &ZEITP;

   data skaldat;
   merge skaldat1(keep=&PERSON &ZEITP score1) skaldat2(keep=&PERSON &ZEITP score2);
   by &PERSON &ZEITP;
   run;

   proc sort data=skaldat;by &ZEITP;
   proc corr data=skaldat noprint outp=corrdat3;
   var score1 score2;
   by &ZEITP;
   run;

   data corrdat3;
   set corrdat3;
   if _TYPE_='CORR' and _NAME_='SCORE2';
   rename score1=rttp;
   drop _TYPE_ _NAME_ SCORE2;
   run;

   proc sort data=corrdat1;by &ZEITP;
   proc sort data=corrdat2;by &ZEITP;
   proc sort data=corrdat2;by &ZEITP;

   data corrdat;
   merge corrdat1 corrdat2 corrdat3;
   by &ZEITP;
   rttspea=2*rttp/(1+rttp);
   run;

   title1 'DATENBOXZERLEGUNG - MIT REPLIKATION - MUTZ/2001           ';
   title2 '1. Voranalysen: Ueberpruefung der Paralleltestqualitaet   ';
   title3 '1.2. Testhalbierung Reliabilitaetskoeffizienten           ';
   footnote1 'rtt1=Cronbach Alpha -Test1 rtt2=Cronbach Alpha - Test2';
   footnote2 'rttp=Paralleltestkorrelation rspae=Spearman-Brown';

   proc print data=corrdat;
   var &ZEITP rtt1 rtt2 rttp rttspea;
   run;
   footnote1;footnote2;


   proc sort data=basdat;
   by &ZEITP &PERSON &TEST;
   run;



  /*2. VORBEREITENDE ANALYSEN UND DATENTRANSFORMATIONEN*/
  /*2.1. Erzeugung der zentralen Summen-und Mittelwertsdateien */

   proc summary data = basdat sum;
   var &VARIAB;
   class  &TEST &PERSON &ZEITP;
   output out = SUMDAT SUM
                (&VARIAB)
                = &VARIAB;
   run;


   data gsum sfsit sfper sfinter basis;
   set sumdat;
   if _type_ = 0 then output gsum;
   if _type_ = 1 then output sfsit;
   if _type_ = 2 then output sfper;
   if _type_ = 3 then output sfinter;
   if _type_ = 7 then output basis;
   run;

   proc summary data = basdat;
   var &VARIAB;
   class  &PERSON &ZEITP ;
   output out = MITDAT MEAN
                (&VARIAB)
                = &VARIAB;
   run;

   data gsum1 sfsit1 sfper1 sfinter1;
   set mitdat ;
   if _type_ = 0 then output gsum1;
   if _type_ = 1 then output sfsit1;
   if _type_ = 2 then output sfper1;
   if _type_ = 3 then output sfinter1;
   run;

  /* 2.2 Output der Gesamtdatei und den einzelnen Mittelwerten*/

   title1 'DATENBOXZERLEGUNG - MIT REPLIKATION - MUTZ/2001      ';
   title2 '2.1. Vektoren der Mittelwerte der Variablen          ';
   title3 '2.1.1. Gesamtmittelwerte                             ';
   title4;
   proc print data= gsum1;
   var &VARIAB;
   run;

   title1 'DATENBOXZERLEGUNG - MIT REPLIKATION - MUTZ/2001    ';
   title2 '2.1. Vektoren der Mittelwerte der Variablen        ';
   title3 '2.1.2. Mittelwerte ueber die Situationen           ';
   title4;
   proc print data=sfsit1;
   var &ZEITP &VARIAB;
   run;

   title1 'DATENBOXZERLEGUNG - MIT REPLIKATION - MUTZ/2001 ';
   title2 '2.1. Vektoren der Mittelwerte der Variablen     ';
   title3 '2.1.3. Mittelwerte ueber die Personen           ';
   title4;
   proc print data=sfper1;
   var &PERSON &VARIAB;
   run;



   /* 3. MULTIVARIATE KREUZPRODUKTZERLEGUNG MIT REPLIKATION*/
   /* 3.1. Einlesen der Dateien in Matrizen des IML-Programms*/

    proc iml;

    reset noprint;


    satz  = {&VARIAB};


    use gsum;
    read all var satz into XG;
    use sfper;
    read all var satz into XFP;
    use sfsit;
    read all var satz into XFS;
    use sfinter;
    read all var satz into XFI;
    use basis;
    read all var satz into X;



    Ng= NROW(X);    /* Gesamtzahl der Beobachtungen*/
    Q = NCOL(X);    /* Anzahl der Variablen*/
    P = NROW(XFP);  /* Anzahl der PERSONEN*/
    K = NROW(XFS);  /* Anzahl der ZEITPUNKTE/SITUATIONEN*/
    n = Ng/(P*K);   /* Anzahl der Beobachtungen innerhalb der Zellen*/



    START IN (A,T);
    T = DIAG(1/SQRT(VECDIAG(A)));
    FINISH;

 /* 3.2. Multivariate Kreuzproduktzerlegung*/

    SStot  = X` * X - XG ` * XG/Ng;
    SSbp   = XFP ` * XFP * 1/(k*n) - XG ` * XG/Ng;
    SSbs   = XFS ` * XFS * 1/(p*n) - XG ` * XG/Ng;
    SSpxs  = XFI ` * XFI * 1/n- SSbp- SSbs - XG`*XG/Ng;
    SSres  = SStot - SSbp - SSbs- SSpxs;
    SStotb = SSbp + SSbs + SSres+ SSpxs;
    SSws   = SStot -SSbs;
    SSwp   = SStot -SSbp;

 /* 4. Multivariate Reliabilitaetskoeffizienten*/

  /*4.1. Multivariater Reliabilitaetskoeffizient-Summenskala*/

    RTTbp = SSbp[+,+]/SStot[+,+];
    RTTbs = SSbs[+,+]/SStot[+,+];
    RTTpxs= SSpxs[+,+]/SStot[+,+];
    RTTtot= RTTbp+RTTbs+RTTpxs;


 /*4.2. Multivariater Reliabilitaetskoeffizient-multivariate
        Spurenkorrelation*/

    Etot = eigvec(SStot);
    Ltot = diag(Etot`*SStot*Etot);
    Lbp  = diag(Etot`*SSbp *Etot);
    Lbs  = diag(Etot`*SSbs *Etot);
    Lpxs = diag(Etot`*SSpxs*Etot);
    Ltrue= diag(Etot`*(SSbp+SSbs+SSpxs)*Etot);


    TTbp =sum(vecdiag(Lbp)  /vecdiag(Ltot))/q;
    TTbs =sum(vecdiag(Lbs)  /vecdiag(Ltot))/q;
    TTpxs=sum(vecdiag(Lpxs) /vecdiag(Ltot))/q;
    TTtot=sum(vecdiag(Ltrue)/vecdiag(Ltot))/q;


  /*4.3. Multivariater Reliabilitaetskoeffizient-maximierte
         Reliabilitaet*/

    Etot = eigvec(SStot);
    Etot = Etot[,1];/*Erstellung des Gewichtsvektor = groesster
                      Eigenvektor*/

    Ltot = diag(Etot`*SStot*Etot);
    Lbp  = diag(Etot`*SSbp *Etot);
    Lbs  = diag(Etot`*SSbs *Etot);
    Lpxs = diag(Etot`*SSpxs*Etot);
    Ltrue= diag(Etot`*(SSbp+SSbs+SSpxs)*Etot);


    RMAXbp =sum(vecdiag(Lbp)  /vecdiag(Ltot));
    RMAXbs =sum(vecdiag(Lbs)  /vecdiag(Ltot));
    RMAXpxs=sum(vecdiag(Lpxs) /vecdiag(Ltot));
    RMAXtot=sum(vecdiag(Ltrue)/vecdiag(Ltot));


  /*4.4. Generalisierbarkeitstheorie*/

    Ubp =SSbp [+,+]/(SSbp [+,+]  + SSres[+,+]);
    Ubs =SSbs [+,+]/(SSbs [+,+]  + SSres[+,+]);
    Upxs=SSpxs[+,+]/(SSpxs[+,+]  + SSres[+,+]);


 /* 4.5. Erstellung der Korrelationsmatrizen mit Normierung
         an der totalen Kreuzproduktmatrix*/

    RUN IN (SStot,S);
    Rtotc = S * SStot * S;

    Rbpc  = S * SSbp  * S;

    Rbsc  = S * SSbs  * S;

    Rpxsc = S * SSpxs * S;

    Rwpc  = S * SSwp  * S;

    Rwsc  = S * SSws  * S;

    Rresc = S * SSres * S;



   /*4.6. Erstellung der Korrelationsmatrizen mit Normierung
          an der jeweiligen Quadratsumme der Kreuzproduktmatrix, sprich
          der Diagonalen */

    RUN IN (SStot,S);
    Rtot = S * SStot * S;

    RUN IN (SSbp,SBP);
    RbP  = SBP * SSbp  * SBP;

    RUN IN (SSbs,SBS);
    RbS  = SBS * SSbs  * SBS;

    RUN IN (SSpxs,SI);
    Rpxs = SI * SSpxs * SI;

    RUN IN (SSwp,SWP);
    RwP  = SWP * SSwp  * SWP;

    RUN IN (SSws,SWS);
    RwS  = SWS * SSws  * SWS;

    RUN IN (SSres,Sres);
    Rres = Sres * SSres * Sres;

    /*Test, dass die Residualmatrix eine Nullmatrix ist*/
    R_TEST=-2*k*p*log(abs(det(Rres)));
    df=q*(q-1)/2;
    PROB_R=1-probchi(R_TEST,df);




    /*4.6. T-Tests der Korrelationen der einzelnen Matrizen*/
    /*    Zweifaktorielle Varianzanalyse*/

    AI=SHAPE(1,q,q);
    AII=DIAG(AI);

    QR=(AI-Rtot##2)+AII;
    Ttot=((Rtot*(k*p*n-2)##0.5)/(QR##0.5));
    Ttot=Ttot-DIAG(Ttot)+AII;
    Ptot=AI-PROBT(ABS(Ttot),k*p*n-1);

    QR=(AI-Rbp##2)+AII;
    Tbp=((Rbp*(p-2)##0.5)/(QR##0.5));
    Tbp=Tbp-DIAG(Tbp)+AII;
    Pbp=AI-PROBT(ABS(Tbp),p-1);


    QR=(AI-Rbs##2)+AII;
    Tbs=((Rbs*(k-2)##0.5)/(QR##0.5));
    Tbs=Tbs-DIAG(Tbs)+AII;
    Pbs=AI-PROBT(ABS(Tbs),k-1);


    QR=(AI-Rpxs##2)+AII;
    Tpxs=((Rpxs*(k*p-2)##0.5)/(QR##0.5));
    Tpxs=Tpxs-DIAG(Tpxs)+AII;
    Ppxs=AI-PROBT(ABS(Tpxs),(k-1)*(p-1));

    QR=(AI-Rwp##2)+AII;
    Twp=((Rwp*(p*k*n-2)##0.5)/(QR##0.5));
    Twp=Twp-DIAG(Twp)+AII;
    Pwp=AI-PROBT(ABS(Twp),p*(k*n-1));

    QR=(AI-Rws##2)+AII;
    Tws=((Rws*(k*p*n-2)##0.5)/(QR##0.5));
    Tws=Tws-DIAG(Tws)+AII;
    Pws=AI-PROBT(ABS(Tws),k*(p*n-1));

    QR=(AI-Rres##2)+AII;
    Tres=((Rres* (p*k*n-2)##0.5)/(QR##0.5));
    Tres=Tres-DIAG(Tres)+AII;
    Pres=AI-PROBT(ABS(Tres),p*k*(n-1));


    free QR AI AII;

   /* 4.7. Output der Ergebnisse*/



    title1 'DATENBOXZERLEGUNG - MIT REPLIKATION - MUTZ/2001    ';
    title2 '3. Ergebnisse der Datenboxzerlegung                ';
    title3 'Korrelationsmatrizen-Signifikanzen                 ';
    title4;


    print " Zahl der Variablen: ",,Q;
    print " Zahl der Personen: ",,P;
    print " Zahl der Situationen: ",,K;
    print " Gesamtzahl der Beobachtungen: ",,Ng;
    print " Zahl der Beobachtungen pro Zelle: ",,n;


    print " ERGEBNISSE  DER DATENBOXZERLEGUNG MIT REPLIKATION ";
    print "                                                   ";

    print "3.1. CROSSPRODUCT-MATRICES";
    print " CROSSPRODUCT-MATRIX - total - SStot                        ",,SStot[r=satz c=satz];
    print " CROSSPRODUCT-MATRIX - zwischen Personen - SSbp             ",,SSbp [r=satz c=satz];
    print " CROSSPRODUCT-MATRIX - zwischen Situationen - SSbs          ",,SSbs [r=satz c=satz];
    print " CROSSPRODUCT-MATRIX - Interaktion Person*Situation - SSpxs ",,SSpxs[r=satz c=satz];
    print " CROSSPRODUCT-MATRIX - innerhalb von Personen - SSwp        ",,SSwp [r=satz c=satz];
    print " CROSSPRODUCT-MATRIX - innerhalb von Situationen - SSws     ",,SSws [r=satz c=satz];
    print " CROSSPRODUCT-MATRIX - Fehleranteil - SSRres                ",,SSres[r=satz c=satz];


    print "3.2. CORRELATION-MATRIX an der TOTALEN KOVARIANZMATRIX normiert";
    print " CORRELATION-MATRIX - total - Rtot                        ",,Rtotc[r=satz c=satz];
    print " CORRELATION-MATRIX - zwischen Personen - Rbp             ",,Rbpc [r=satz c=satz];
    print " CORRELATION-MATRIX - zwischen Situationen - Rbs          ",,Rbsc [r=satz c=satz];
    print " CORRELATION-MATRIX - Interaktion Person*Situation - Rpxs ",,Rpxsc[r=satz c=satz];
    print " CORRELATION-MATRIX - innerhalb von Personen - Rwp        ",,Rwpc [r=satz c=satz];
    print " CORRELATION-MATRIX - innerhalb von Situationen - Rws     ",,Rwsc [r=satz c=satz];
    print " CORRELATION-MATRIX - Fehleranteil - Rres                 ",,Rresc[r=satz c=satz];


    print "3.3. CORRELATION-MATRIX an der EINZELNEN KOVARIANZMATRIX normiert";
    print " CORRELATION-MATRIX - total - Rtot                       ",,Rtot[r=satz c=satz];
    print " CORRELATION-MATRIX - zwischen Personen - Rbp            ",,Rbp [r=satz c=satz];
    print " CORRELATION-MATRIX - zwischen Situationen - Rbs         ",,Rbs [r=satz c=satz];
    print " CORRELATION-MATRIX - Interaktion Person*Situation - Rpxs",,Rpxs[r=satz c=satz];
    print " CORRELATION-MATRIX - innerhalb von Personen - Rwp       ",,Rwp [r=satz c=satz];
    print " CORRELATION-MATRIX - innerhalb von Situation - Rws      ",,Rws [r=satz c=satz];
    print " CORRELATION-MATRIX - Fehleranteil - Rres                ",,Rres[r=satz c=satz];

    print "3.4. T-TESTS DER KORRELATIONEN - NORMIERT AN EINZELNER KOVARIANZMATRIX";
    print "T-TEST VON Rtot MIT SIGNIFIKANZ: ",,Ttot [r=satz c=satz],
                                               Ptot [r=satz c=satz];
    print "T-TEST VON Rbp  MIT SIGNIFIKANZ: ",,Tbp  [r=satz c=satz],
                                               Pbp  [r=satz c=satz];
    print "T-TEST VON Rbs  MIT SIGNIFIKANZ: ",,Tbs  [r=satz c=satz],
                                               Pbs  [r=satz c=satz];
    print "T-TEST VON Rpxs MIT SIGNIFIKANZ: ",,Tpxs [r=satz c=satz],
                                               Ppxs [r=satz c=satz];
    print "T-TEST VON Rwp  MIT SIGNIFIKANZ: ",,Twp  [r=satz c=satz],
                                               Pwp  [r=satz c=satz];
    print "T-TEST VON Rws  MIT SIGNIFIKANZ: ",,Tws  [r=satz c=satz],
                                               Pws  [r=satz c=satz];
    print "T-TEST VON Rres MIT SIGNIFIKANZ: ",,Tres [r=satz c=satz],
                                               Pres [r=satz c=satz];


    print "3.5. PRUEFUNG: H0: RESIDUALMATRIX=IDENTITAETSMATRIX";
    print "CHI2-Wert=" R_TEST "df=" df "p=" PROB_R;
    print "                                       ";
    print "                                       ";


    print "3.6. MULTIVARIATE RELIABILITAETSTHEORIE";
    print "                                                       ";
    print "3.6.1. Multivariate Reliabilitaet-Summenskala(RTT)";
    print "Multivariate Reliabilitaet - zwischen Personen         ",,Rttbp;
    print "Multivariate Reliabilitaet - zwischen Situationen      ",,Rttbs;
    print "Multivariate Reliabilitaet - Interaktion Person*Situat.",,Rttpxs;
    print "Multivariate Reliabilitaet - TOTAL                     ",,Rtttot;

    print "                                                       ";
    print "3.6.2. Multivariate Reliabilitaet-Spurenkorrelation(TT)";
    print "Multivariate Reliabilitaet - zwischen Personen         ",,TTbp;
    print "Multivariate Reliabilitaet - zwischen Situationen      ",,TTbs;
    print "Multivariate Reliabilitaet - Interaktion Person*Situat.",,TTpxs;
    print "Multivariate Reliabilitaet - TOTAL                     ",,TTtot;


    print "                                                       ";
    print "3.6.3. Multivariate Reliabilitaet-Maximierte Reliabilitaet(RMAX)";
    print "Multivariate Reliabilitaet - zwischen Personen         ",,RMAXbp;
    print "Multivariate Reliabilitaet - zwischen Situationen      ",,RMAXbs;
    print "Multivariate Reliabilitaet - Interaktion Person*Situat.",,RMAXpxs;
    print "Multivariate Reliabilitaet - TOTAL                     ",,RMAXtot;

    print "3.7. MULTIVARIATE GENERALISIERBARKEITSTHEORIE";
    print "                                                            ";
    print "Multivariate Generalisierbarkeit - zwischen Personen        ",,Ubp;
    print "Multivariate Generalisierbarkeit - zwischen Situationn      ",,Ubs;
    print "Multivariate Generalisierbarkeit - zwischen Personen*Situat.",,Upxs;


    free  Ttot Ptot Tbp Pbp Tbs Pbs Twp Pwp Tws Pws Tres Pres Ppxs Tpxs Ppxs
          TTbp TTbs TTpxs TTtot RMAXbp RMAXbs RMAXpxs RMAXtot Ubp Ubs Upxs
          S Sbp Sbs Si Swp Sws Sres SStot SSbp SSpxs SSws SSres ;


    /* 4.8. AUSLESEN DER KORRELATIONSMATRIZEN IN SAS-DATEIEN*/



    VARNAME = {&VARIAB};
    varmat=satz`;

    create CORtot from Rtot  [COLNAME = VARNAME];
    append from Rtot;
    create CORbp from Rbp    [COLNAME = VARNAME];
    append from Rbp;
    create CORbs from Rbs    [COLNAME = VARNAME];
    append from Rbs;
    create CORpxs from Rpxs  [COLNAME = VARNAME];
    append from Rpxs;
    create CORres from Rres  [COLNAME = VARNAME];
    append from Rres;
    create X from varmat [COLNAME={NAME}];
    append from varmat;free varmat;

    free Rres Rbs Rtot Rbp Rpxs Rresc Rbsc Rbpc Rpxsc Rwpc Rwsc;
    quit;


    data dtot (type = corr);
    merge x CORtot;
    rename NAME=_NAME_;
    _type_ = "CORR";
    run;

    data dbp (type = corr);
    merge x CORbp;
    rename NAME=_NAME_;
    _type_ = "CORR";
    run;

    data dbs (type = corr);
    merge x CORbs;
    rename NAME=_NAME_;
    _type_ = "CORR";
    run;

    data dpxs (type = corr);
    merge x CORpxs;
    rename NAME=_NAME_;
    _type_ = "CORR";
    run;

    data dres (type = corr);
    merge x CORres;
    rename NAME=_NAME_;
    _type_ = "CORR";
    run;

    /* 5. FAKTORENANALYSEN DER EINZELNEN KORRELATIONSMATRIZEN*/


    title1 'DATENBOXZERLEGUNG - MIT REPLIKATION - MUTZ/2001                  ';
    title2 '4. Faktorenanalyse - NORMIERUNG an EINZELNER KOVARIANZMATRIX     ';
    title3 '4.1. Faktorenanalyse - TOTALEN Korrelationsmatrix Rtot           ';
    proc factor data = dtot rotate = varimax c;
    run;

    title3 '4.2. Faktorenanalyse - Korrelation ZWISCHEN PERSONEN: Rbp        ';
    proc factor data = dbp rotate = varimax c;
    run;

    title3 '4.3. Faktorenanalyse -Korrelation ZWISCHEN SITUATIONEN: Rbs      ';
    proc factor data = dbs rotate = varimax c;
    run;

    title3 '4.4. Faktorenanalyse - Korrelation INTERAKTION PERSON*SITUAT.Rpxs';
    proc factor data = dpxs rotate = varimax c;
    run;

    title3 '4.5. Faktorenanalyse - Korrelation: FEHLERANTEIL: Rres           ';
    proc factor data = dres rotate = varimax c;
    run;
