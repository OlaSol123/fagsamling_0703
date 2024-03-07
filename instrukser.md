***CASE - Chatbot oppslagsverk for dokumenter*** (Ctrl + Shift + V for preview)

Teknologi: Python, Streamlit, GPT

**Introduksjon**

Dere er en gruppe konsulenter hos IT avdelingen til Produsent AS, en av de viktigste kundene til Deloitte. Produsent AS har *hundrevis* av dokumenter av ulike typer som de sliter å holde styr på. Normalt søk med nøkkelord har hjulpet dem noe med dette problemet, men de er interreserte i om gen-AI drevne chatbotter kunne vært en enda bedre løsning og ønsker at dere skal utforske dette. Grunnet viktigheten til prosjektet har Produsent AS også gitt samme oppgave til en et ukjent antall andre konsulenthus. Hvis ikke deres team finner den beste løsningen opphører samtlige av Deloittes kontrakter med Produsent AS.

I prosjektbeskrivelsen legger kunden stor vekt på løsningen MÅ utformes med hensyn til følgende kriterier:

- Kostnader
- Datasikkerhet
- Personvern (noen av tekstdokumentene inneholder sensitive opplysninger)

**OPPGAVE 1: Sette opp chatbot**

Sjefen hos Produsent AS har lite tro på Copilot Studio og ønsker en annen type implementering. Heldigvis har dere tilgang til en Streamlit Chatbot med en API kobling til GPT som dere kan sette opp slik:

1. Gå inn i github repository-en og lag en codespace
2. skriv 'pip install -r reqs/requirements.txt' i terminalen
3. På linje 10 i chatbot.py: sett inn API nøkkel-en som blir gitt ut 
4. Skriv 'streamlit run chatbot.py' i terminalen
5. Klikk på 'Open in Browser' i boksen som dukker opp nede til høyre

Hvis du har en fane med en chatbot som starter dialog med en hilsen har du fullført oppgave 1.

Ønsker du å skru av chatbotten, hold inn Ctrl + C i terminalen

**OPPGAVE 2: Implementere oppslagsverk for CSV filer**

Denne delen krever at dere tenker dere godt igjennom. Teksten i prompt.txt er en system prompt, dvs. at det er den første meldingen som blir gitt til GPT. Denne er foreløpig ikke utformet for sitt formål. For at system prompten skal fasilitere enn chat som funker som oppslagsverk på dokumenter må dere gjøre to ting med teksten i prompt.txt:

1. Gi instrukser til GPT som gjør at den skjønner sitt oppdrag som oppslagsverk for dokumenter.
2. Gjøre at chatboten kan svare på dokumentene gitt i 'dokumenter' mappen. Her må dere ta stilling til hva slags informasjon system prompten skal inneholde om dokumentene. Ta hensyn til kriteriene gitt i introduksjonen. Fokuser *bare* på CSV filene.

**BONUS** 

Ta stilling til hvordan deres tilnærming kunne blitt oppdatert automatisk ved endringer i dokument mappen. Hvis dere har noen med Python ferdigheter på gruppen deres MÅ dere prøve å programmere en slik løsning. Gjør det i csv_to_prompt.py. Bruk gjerne PairD som hjelp.

**OPPGAVE 3**

Ta stilling til hvordan man kunne utvidet løsningen til PDF dokumenter. Igjen så må dere ta hensyn til kriteriene gitt i introduksjonen. Det er gitt noen PDF filer som eksempler i 'dokumenter' mappen (Tips: last gjerne ned PDF Preview under Extensions for å se disse lettere).

 

