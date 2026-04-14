<div style="display: flex; align-items: flex-start; gap: 1rem; margin-bottom: 2rem;">
  <img src="../img/Jens.jpg" width="180" class="shadow" style="flex-shrink: 0;" alt="Mein Profilbild – Technischer Writer & Information Architect" />
  <div>

Ich arbeite an der Schnittstelle von Technik, Struktur und Kommunikation.  
Meine Schwerpunkte liegen auf moderner Dokumentation, Informationsarchitektur und klaren, wartbaren Workflows. Die Seite zeigt meine methodischen, technischen und konzeptionellen Kompetenzen aus 30 Jahren Arbeit an DDScad und angrenzenden Projekten.

  </div>
</div>

## Analyse & Architektur

!!! tip "Tätigkeitsanalyse (2008/2009)"
    **Motivation und Ziel:** 
    Nutzerzentrierte und aufgabenorientierte Dokumentation für DDScad, welche die realen Arbeitsprozesse der Zielgruppe berücksichtigt

    ??? abstract "Schritt 1 - Theoriegeleitete Erhebung und Auswertung"

        **Methode**

        Theoriegeleitete Erhebung und Auswertung (10 leitfaden-gestützte narrative Interviews mit Elektroplaner:innen): Die Tätigkeitstheorie (Leontjew) war die Basis zur Analyse von Handlungsstrukturen. Das Modell vom Tätigkeitssystem (Engeström) bildet das Gerüst zur Berücksichtigung äußerer Impulse auf Handlungen der Zielgruppenangehörigen. 

        **Ergebnisse**

        Rekonstruktion der Tätigkeit der Zielgruppe als kohärente Beschreibung, welche

        - die Struktur der Tätigkeit (Aufgaben, Anforderungen, kritische Momente, typische Handlungen) abbildet
        - als Grundlage für die nachfolgende Prozessanalyse dient

        **Nachweis/Beispiel**

        Master-Thesis:

        - Kap. 1.2 Aufgabenstellung
        - Kap. 4 Vorbereitung und Durchführung der Datenerhebung
        ??? abstract "Rekonstruktion der Tätigkeit"
            
            <embed src="../files/01_Beleg_MasterThesis_Auszug_TabellarischeAnalyse.pdf" type="application/pdf" width="100%" height="600px" />

    ??? abstract "Schritt 2 - Tabellarische Prozessanalyse"

        **Methode**

        Tabellarische Prozessanalyse der rekonstruierten Tätigkeit bis zum Übergang auf Handlungen am Planungssystem. Das Verfahren integriert:
        - Hierarchische Struktur der Tätigkeit (Tätigkeiten, Handlungen, Operationen; Leontjew:)
        - Handlungsfeldmodell (Ziele vs. Handlungsoptionen; Oesterreich)
        - Regulationsebenen von Handlungen (Volpert: intellektuelle, perzeptiv-begriffliche, sensorisch-motorische Steuerung)

        **Ergebnisse**

        - Tabellarische aufgeschlüsselte Darstellung der Tätigkeit, bei der letztlich jeder Handlung im Prozess ein Handlungsmuster am Planungssystem gegenübersteht 
        - Eine Liste aller Handlungs-muster am Planungssystem (welche direkt beschrieben werden können oder weiter untersucht werden müssen)
        - Erkennung identischer oder ähnlicher Handlungsmuster am Planungssystem für verschiedene Prozessschritte


        **Nachweis/Beispiel**

        Master-Thesis:
        Kap. 6 Analyse der rekonstruierten Tätigkeit

!!! tip "Modulare Dokumentationsarchitektur (2012 - 2025)"
    **Motivation und Ziel:** Wiederverwendbare Informationsbausteine, um Redundanzen zu vermeiden und Aktualisierungen zu vereinfachen

    ??? abstract "Zielerreichung"

        **Methode**

        - Je ein Informationsbaustein zur Beschreibung jeweils eines Parameters oder Steuerelements 
        - Ableitung von Topics aus Handlungsmustern (Master-Thesis)
        - Single-Sourcing in **MadCap Flare**.

        **Ergebnisse**

        100% modularisiertes Dokumentationsprojekt, 0% Redundanzen

        **Nachweis/Beispiel**

        Schriftliche Arbeit zum tekom-Zertifikat, Kapitel 4

## Layout & Konzeption

!!! tip "Nutzerfreundliche UI/UX-Gestaltung der kontextsensitiven Hilfe (2013 - 2025)"
    Platzsparendes, nutzer-orientiertes Layout, das maximale Informations-dichte mit Sichtbarkeit der Hilfe während der Nutzung verbindet. Trennung von WAS (Beschreibung) und WIE (Handlungsanleitung)

    ??? abstract "Zielerreichung"

        **Methode**

        - Dockingfenster (Hilfe bleibt neben DDScad sichtbar
        - Registerkarten zur Trennung: Funktion | Anwendung | WebLinks
        - Aufklappbare Bereiche für vertiefende Informationen

        **Ergebnisse**

        Standardisiertes, aber flexibles Layout-System für die kontext-sensitive Hilfe, welches sich beliebig skalieren und anpassen lässt. Die Registerkarten der verschiedenen Ebenen lassen sich je nach Bedarf aktivieren oder deaktivieren.

        **Nachweis/Beispiel**

        Schriftliche Arbeit zum tekom-Zertifikat, Kapitel 4

!!! tip "Komplexe Workflows übersichtlich darstellen und erklären (2018 - 2025)"
    Gesamtabläufe komplexer Prozesse sollen im Überblick erfassbar sein, möglichst ohne Notwendigkeit zum Scrollen. Für jeden Schritt sollen relevante Informationen abrufbar sein. Zur eigenen  Positionsbestimmung soll der jeweils aktive Schritt deutlich erkennbar sein

    ??? abstract "Zielerreichung"

        **Methode**

        - Schrittweise Aufteilung des Workflows in abgeschlossene Einheiten und Visualisierung als Diagramm (technisch gelöst als Tabelle)
        - Für jeden Schritt per Mausklick abrufbar: Handlungsanleitungen 
        - Aktiver Prozessschritt ist farblich im Diagramm hervorgehoben 
        - technischer Hintergrund: „onclick“-Event-Handler steuern die Sichtbarkeit von div-Containern


        **Ergebnisse**

        Nutzer:innen können sich tief gestaffelte Prozesse und Handlungsabläufe selbstständig erarbeiten. Benötigte Detailinformationen sind abrufbar, ohne dass sich das wesentliche Bild verändert. Der Gesamtüberblick bleibt erhalten, die eigene Position im Prozess ist klar erkennbar.

        **Nachweis/Beispiel**

        Thema im Online-Handbuch:
        - Gebäudemodell auf importiertem Grundriss
        - Heizlast berechnen

!!! tip "Beschreibung GUI (2020 - 2025)"
    Orientierung für Nutzer:innen über die Benutzeroberfläche und die darin enthaltenen Funktionsbereiche

    ??? abstract "Zielerreichung"

        **Methode**

        - Bild der Benutzeroberfläche als Grundlage für eine Image-Map, ge-gliedert nach Funktionsbereichen 
        - Mausklick auf einen Bereich der Image-Map aktiviert einen „onclick“ Event Handler, welcher den aktuell sichtbaren div-Container deaktiviert und den adressierten aktiviert

        **Ergebnisse**

        Nutzer:innen können sich anhand eines einheitlichen Bildes über Bedeutung und Anwendung der verschiedenen Funktionsbereiche informieren. Der Grundaufbau der Seite bleibt unverändert, der Kontext wird nicht verlassen.

        **Nachweis/Beispiel**

        Thema im Online-Handbuch:
        - Benutzeroberfläche auf Modellebene

!!! tip "Beschreibungen unter Einbeziehung des GUI (2020 - 2025)"
    Wissensvermittlung über Funktionalitäten, bei denen die zugehörigen Handlungen mehrere Funktionsbereiche des GUI berühren und die Visualisierung des Gesamtzusammenhangs notwendig erscheint

    ??? abstract "Zielerreichung"

        **Methode**

        - Zweispaltige Tabelle als Grundge-rüst: definierte Spaltenbreite für ein Bild des GUI und variabel für Texte
        - Textteil enthält Informationen und weitere Auswahlmöglichkeiten (z. B. über Handlungsoptionen). 
        - Der Mausklick auf eine Auswahl-möglichkeit aktiviert einen „onclick“ Event Handler, welcher den aktuell sichtbaren div-Container deaktiviert und den adressierten aktiviert. 
        - Das Bild im aktiven Container illus-triert die Beschreibung im Textteil.

        **Ergebnisse**

        Nutzer:innen können sich den beschriebenen Funktions-komplex systematisch erarbeiten. Großflächige GUI-Visualisierungen erleichtern das Verständnis.

        **Nachweis/Beispiel**

        Thema im Online-Handbuch:
        - Ansichten, Perspektiven, Navigation

## Qualität

!!! tip "Terminologie (2018 - 2025)"
    Verständlichkeit und Kostensenkung durch terminologische Konsistenz und fachgerechte Benennungsbildung in der  Benutzeroberfläche von DDScad

    ??? abstract "Zielerreichung"

        **Methode**

        - Eigeninitiative: Entwicklung einer begriffsorientierten Terminologie-Datenbank mit Benennungs-autonomie (Deutsch / Englisch / Norwegisch / Niederländisch; Plattform: FileMaker)
        - Erfassung relevanter Begriffe und der verwendeten Benennungen
        - Klassifizierung der erfassten Benennungen (bevorzugt, erlaubt, verboten usw.) nach Recherche und Rücksprache mit Domain Experts
        - Beharrliche Ansprache der Problematik bei Stakeholdern

        **Ergebnisse**

        - Höhere Sensibilität für Terminologiefragen im Team; 
        - unternemensweit verfügbares und genutztes Recherchinstrument
        - Bereitstellung der Vorzugs- und erlaubten Benennungen für den Übersetzungsprozess als Excel Sheet

        **Nachweis/Beispiel**

        Interne Unterlagen – heute nicht mehr zugänglich


!!! tip "DDScad-Funktionalität (1995 - 2025)"
    Erleichterung der Beschreibbarkeit durch hohe Produktqualität 

    ??? abstract "Zielerreichung"

        **Methode**

        - Begleitung laufender Entwicklungen aus Nutzerperspektive
        - Tests, Rückfragen, Bug Reporting

        **Ergebnisse**

        - Verbesserung von UI-Texten
        - terminologische Konsistenz
        - gelegentlich: Aufdeckung von Konzeptlücken, Fehlfunktionen als Impulse für Verbesserungen

        **Nachweis/Beispiel**

        Interne Unterlagen – heute nicht mehr zugänglich

## Übersetzung

!!! tip "Zusammenarbeit mit externem Dienstleister (2018 - 2023)"
    Schonung eigener Ressourcen

    ??? abstract "Zielerreichung"

        **Methode**

        - Datenaustausch via MadCap Lingo 
        - Bereitstellung Terminologie

        **Ergebnisse**

        - Übersetzte Flare-Projekte (Englisch, Niederländisch, Norwegisch)

        **Nachweis/Beispiel**

        Interne Unterlagen – heute nicht mehr zugänglich


!!! tip "Eigene Übersetzung (2024 - 2025)"
    Zeitersparnis

    ??? abstract "Zielerreichung"

        **Methode**

        - Direkter Import des Flare-Projekts nach memoQ
        - DeepL-unterstützte Übersetzung
        - Export als übersetztes Flare-Objekt

        **Ergebnisse**

        - Mehr Zeit für Authoring
        - mehr Kontrolle über Prozess
        - Kostenreduzierung: Geplante Budgetsumme von € 25.000,- blieb unangetastet

        **Nachweis/Beispiel**

        Interne Unterlagen – heute nicht mehr zugänglich

## Historische Projekte

!!! tip "Gedruckte Handbücher für Disziplinen „Elektro“ & „Heizung / Sanitär / Lüftung“ (2005 - 2012)"
    Praxisnahe Anleitungen für Nutzer:innen der jeweiligen Disziplinen.

    ??? abstract "Zielerreichung"

        **Methode**

        - Strukturierung nach Erkenntnissen aus der Master-Thesis
        - starke Orientierung auf geeignete Text-Bild-Kombination

        **Ergebnisse**

        Standardwerk für DDScad-Nutzer:innen bis 2012; Grundlage für Migration zu digitalen Formaten

        **Nachweis/Beispiel**

        Digitalisierte historische Handbücher (öffentlich zugänglich über YUMPU)


!!! tip "Schulungsdokumentation (2010 - 2015)"
    Didaktische Aufbereitung des Schulungsablaufes für DDScad-Elektro

    ??? abstract "Zielerreichung"

        **Methode**

        - Strukturierung gemäß Schulungsablauf
        - starke Orientierung auf geeignete Text-Bild-Kombination
        - Querverweise zum Online-Handbuch

        **Ergebnisse**

        Dokument zur Unterstützung während und nach einer absolvierten Schulung: 
        „DDS-CAD Elektro – Planung von Starkstromanlagen“

        **Nachweis/Beispiel**

        Schulungsunterlagen (Archiv)

## Tools & Methoden

!!! tip "MadCap Flare (2005 - 2025)"
    Allgemeiner text ... warum Flare

    ??? abstract "Online-Hilfe und Online-Handbuch für das Planungssystem DDScad"
        Effiziente, wiederverwendbare und übersetzbare Dokumentation für DDScad

        **Methode**

        • Single-Sourcing
        • Kennzeichnung bedingter Texte
        • modulare Topics (Snippets)
        • Variablen als UI-Textbaustein 

        **Ergebnisse**

        • 100% modularisierte Dokumentation 
        • Übersetzbarkeit/Aktualisierbar-keit durch Variablen als Verweis auf UI-Texte 

        **Nachweis/Beispiel**

        Schriftliche Arbeit zum tekom-Zertifikat, Kapitel 5


    ??? abstract "Analyse großer Textkörper auf festgelegte Kriterien"
        Filterung und Zusammenstellung von Informationen ausgewählter Kategorien aus großen Textkörpern

        **Methode**

        • Import des Textkörpers 
        • Kennzeichnung von Abschnitten nach Kriterien als „Bedingte Texte“
        • Kompilierung in neues Dokument

        **Ergebnisse**

        • Strukturierte Auswertung von Interview-Transskripten

        **Nachweis/Beispiel**

        Master-Thesis, Kapitel 4.6.4

!!! tip "FileMaker (2018 - 2025)"
    Ein allgemeiner Text ... warum FileMaker, verschiedene Anwendungen

    ??? abstract "Begriffsorientierte Terminologie-Datenbank mit Benennungsautonomie"

        **Methode**

        Eigenständige Entwicklung einer Datenbank zur Terminologie-Erfassung und Verwaltung mit Exportfunktionen

        **Ergebnisse**

        ca. 1.200 Einträge – genutzt von Kollegen zur Recherche und zur Bereitstellung erlaubter Benen-nungen im Übersetzungsprozess

        **Nachweis/Beispiel**

        Interne Unterlagen – heute nicht mehr zugänglich


    ??? abstract "Gegenüberstellung der UI-Texte aller DDScad-Sprachversionen"

        **Methode**

        Eigenständige Entwicklung einer Datenbank zum Import bereitgestellter Ressource-Daten

        **Ergebnisse**

            • Werkzeug zur sprachüber-greifenden Recherche in UI-Texten und zu deren Prüfung
            • Grundlage für systematische Qualitätssicherung sprachlicher Aspekte im GUI von DDScad

        **Nachweis/Beispiel**

        Interne Unterlagen – heute nicht mehr zugänglich

!!! tip "Atlassian Jira/Confluence (2020 - 2025)"
    Teilnahme an agilen Entwicklungs- und Dokumentationsprozessen

    ??? abstract "Zielerreichung"

        **Methode**

        • Jira im Entwicklungsprozess zur Definition und Zuweisung von Auf-gabenstellungen als Ticketsystem
        • Confluence zur internen Dokumentation von Strukturen und Abläufen (Wissensmanagement)

        **Ergebnisse**

        • Überblick über den Projektstand
        • Kontrolle über den Projektverlauf
        • interner Austausch

        **Nachweis/Beispiel**

        Interne Unterlagen – heute nicht mehr zugänglich

!!! tip "Miro (2020 - 2025)"
    Visualisierungen von Zusammenhängen verschiedenster Art

    ??? abstract "Zielerreichung"

        **Methode**

        • Zur eigenen Strukturierung
        • Für Präsentationen, zur Argumen-tation und Diskussion im Team

        **Ergebnisse**

        Große Unterstützung und angenehmeres Arbeiten in konzeptionellen Prozessen

        **Nachweis/Beispiel**

        Interne Unterlagen – heute nicht mehr zugänglich


## Soft Skills

!!! tip "Beharrlichkeit & Eigeninitiative (1995 - 2025)"
    Qualität durchsetzen, auch ohne offizielle Unterstützung.

    ??? abstract "Zielerreichung"

        **Methode**

        • Terminologie-Datenbank als "U-Boot-Projekt"
        • Ständige Sensibilisierung (Team) 
        • Sorgfältigkeit in Bug Reports

        **Ergebnisse**

        • Bessere Beschreibbarkeit 
        • Positiver Einfluss auf die Nutzerfreundlichkeit

        **Nachweis/Beispiel**

        Interne Unterlagen – heute nicht mehr zugänglich

!!! tip "Analyse (2009 - 2025)"
    Nutzerbedürfnisse verstehen, um Dokumentation praxistauglich zu gestalten

    ??? abstract "Zielerreichung"

        **Methode**

        • Narrative Interviews führen und auswerten.
        • Nutzerrelevante Normen und Regeln verstehen 

        **Ergebnisse**

        • Aufgabenorientierter Aufbau 
        • Fachgerechte Terminologie 
        • Folgerichtige Abläufe

        **Nachweis/Beispiel**

        Master-Thesis, Kap. 5–6

!!! tip "Erklären und beschreiben"
    Komplexe Sachverhalte so vermitteln, dass andere sie schnell verstehen, einordnen und sicher anwenden können – unabhängig von Vorwissen oder Kontext

    ??? abstract "Zielerreichung"

        **Methode**

        • Reduktion auf das Wesentliche ohne Bedeutungsverlust 
        • Nutzung von Beispielen, Analogien und Perspektivwechseln 
        • Präzise, verständliche Sprache 
        • Anpassung der Erklärung an die Bedürfnisse des Gegenübers

        **Ergebnisse**

        • Menschen verstehen Zusammenhänge schneller und sicherer 
        • Missverständnisse werden reduziert, Entscheidungen erleichtert 
        • Komplexe Themen werden zugänglich, auch für fachfremde Personen 
        • gelegentlich die Frage, wie ich etwas erklären würde 

        **Nachweis/Beispiel**

        Rückmeldungen aus dem beruflichen und privaten Umfeld

!!! tip "Zuhören und fragen"
    Andere Menschen wirklich verstehen – ihre Anliegen, Bedürfnisse, Unsicherheiten und Prioritäten – um Missverständnisse zu vermeiden und tragfähige Lösungen zu ermöglichen

    ??? abstract "Zielerreichung"

        **Methode**

        • Aktives Zuhören und geduldiges Ausredenlassen 
        • Klärende, offene und präzise Fragen 
        • Zusammenfassen und Spiegeln zur Sicherung des gemeinsamen Verständnisses 
        • Perspektivwechsel, um Situationen aus Sicht des Gegenübers zu erfassen 
        • Nachfragen bis zur Klärung der tatsächlichen Ursache eines Problems

        **Ergebnisse**

        • Menschen fühlen sich ernst genommen und verstanden 
        • Konflikte und Missverständnisse werden früh erkannt und entschärft 
        • Gespräche verlaufen strukturiert und zielgerichtet 
        • Vertrauen, wenn „der Kern“ des Anliegens erkannt ist

        **Nachweis/Beispiel**

        Rückmeldungen aus dem beruflichen und privaten Umfeld (u. a. durch meine Frau)

[Zu meiner Erfahrung →](experience.md)