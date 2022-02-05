---
authors:
- Vít Černý
title: Výroková logika
layout: note
date: 2022-02-04
subject: Matematika
grades:
- G5
topics:
- Logika
teachers:
- Ladislav Zemánek
math: true
---




## Výrok  
  - Je každé tvrzení , o kterém má smysl (popř. je možno) prohlásit, zda je či není pravdivé  
  - Má tvar oznamovací věty  
  - Pravdivostní hodnota výroku  
    - $0$ je nepravda  
    - $1$ je pravda  

## Negace výroku  
  - Negace výrokuje výrok, který vylučuje platnost výroku (má opačnou pravdivostní hodnotu)  
  - Negaci výroku $v$ označujeme $\neg v$  
    - pokud $p(x) = 1$, potom $p(\neg x) = 0$  
  - _Aspoň_, _nejvýše_ a jejich negace  
    - Řekneme-li, že nějaká množina má aspoň k prvků, znamená to, že počet jejích prvků je větší nebo roven číslu $k$  
      - $p(v)$ – Množina M má aspoň k prvků.  
      - $p(\neg v)$ – Množina M má nejvýše k − 1 prvků.  
    - Řekneme-li, že nějaká množina má nejvýše k prvků, znamená to, že počet jejích prvků je menší nebo roven číslu $k$  
      - $p(u)$ – Množina $M$ má nejvýše $k$ prvků.  
      - $p(\neg u)$ – Množina $M$ má aspoň $k + 1$ prvků.  
    - Příklady  
      - `Ve třídě je aspoň 33 studentů`  
        - Negace: `Ve třídě je nanejvýš 32 studentů`  
      - `Do kina přijde nanejvýš 150 diváků`  
        - Negace: `Do kina přijde aspoň 151 diváků`  

## Složené výroky  
  - **Konjunkce**  
    - $a \wedge b$  
    - {{table}}  
      - $a$  
        - $b$  
          - $a \wedge b$  
      - 1  
        - 1  
          - **1**  
      - 1  
        - 0  
          - 0  
      - 0  
        - 1  
          - 0  
      - 0  
        - 0  
          - 0  
    - Logické spojky _a_, _i_, _zároveň_  
  - **Disjunkce**  
    - $a \vee b$  
    -   
      - $a$  
        - $b$  
          - $a \vee b$  
      - 1  
        - 1  
          - **1**  
      - 1  
        - 0  
          - **1**  
      - 0  
        - 1  
          - **1**  
      - 0  
        - 0  
          - 0  
    - Logická spojka _nebo_  
  - **Implikace**  
    - $a \Rightarrow b$  
    -   
      - $a$  
        - $b$  
          - $a \Rightarrow b$  
      - 1  
        - 1  
          - **1**  
      - 1  
        - 0  
          - 0  
      - 0  
        - 1  
          - **1**  
      - 0  
        - 0  
          - **1**  
    - Logická spojka _jestliže_, _pak_  
  - **Ekvivalence**  
    - $a \Leftrightarrow b$  
    - {{table}}  
      - $a$  
        - $b$  
          - $a \Leftrightarrow b$  
      - 1  
        - 1  
          - **1**  
      - 1  
        - 0  
          - 0  
      - 0  

        - 1  
          - 0  
      - 0  
        - 0  
          - **1**  
    - Logická spojka _jestliže tehdy_, _když_  

## Negace složených výroků
    - **Výrok**  
      - **Negace výroku**  
        - **Tautologie negace**  
    - $x\wedge y$  
      - $\neg(x\wedge y)$  
        - $\neg x\vee \neg y$  
    - $x\vee y$  
      - $\neg(x\vee y)$  
        - $\neg x\wedge\neg y$  
    - $x\Rightarrow y$  
      - $\neg(x\Rightarrow y)$  
        - $x\wedge\neg y$  
    - $x\Leftrightarrow y$  
      - $\neg(x\Leftrightarrow y)$  
        - $(x\wedge\neg y)\vee(\neg x\wedge y)$  

## Kvantifikované výroky  
  - **Obrácená implikace**  
    - Obrácenou implikací $u \Rightarrow v$ rozumíme $v \Rightarrow u$  
    - Pravdivostní hodnoty původní a obrácené implikace spolu nesouvisí  
  - **Obměněná implikací**  
    - Obměněnou implikací $u \Rightarrow v$ rozumíme $\neg v \Rightarrow \neg u$  
    - Implikace a její obměna mají stejné pravdivostní hodnoty  
  - **Obecný kvantifikátor**  
    - Obecným kvantifikátorem rozumíme slovo či slovní spojení, které má význam _každý_, _všechna_, _pro každý_, _pro všechna_  
    - Symbolicky značíme $\forall$  
  - **Existenční kvantifikátor**  
    - Značíme $\exists$  
    - Existenčním kvantifikátorem rozumíme slovo či slovní spojení, které má význam _existuje_, _alespoň jeden_ apod.  
  - Kvantifikované výroky  
    - **Obecný výrok**  
      - Má tvar: Pro každé _x_ z množiny _M_ platí vlasntost _V_  
        - Symbolicky $\forall x \in M:V$  
        - Př.: Pro každé reálné číslo platí, že jeho druhá mocnina je číslo nezáporné.  
    - **Existenční výrok**  
      - Má tvar: Existuje _x_ z množiny _M_, pro které platí vlastnost _V_  
        - Symbolicky: $\exists \in M:V$  
        - Př.: Existuje přirozené číslo, jehož odmocnina není číslo přirozené  
    - Negace jsou ez  
    - Další kvantifikované výroky  
      - Když řekneme, že množina _M_ má PRÁVĚ _k_ prvků, kde _k_ je libovolné přirozené číslo, znamená to, že prvků množiny _M_ není ani více ani méně než _k_, je jich přesně _k_.  
      - Když řekneme, že množina _M_ má NEJVÝŠE _k_ prvků, kde _k_ je libovolné přirozené číslo, znamená to, že prvků množiny _M_ je právě _k_ nebo méně než _k_.  
      - Když řekneme, že množina _M_ má ALESPOŇ k prvků, kde _k_ je libovolné přirozené číslo, znamená to, že prvků množiny _M_ je právě _k_ nebo více než _k_.  
