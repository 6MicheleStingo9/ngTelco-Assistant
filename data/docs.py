from langchain.schema import Document

offers_docs = [
    Document(
        page_content="""
        Scopri l'essenziale con 'basic talk', l'offerta pensata per chi non ha bisogno di fronzoli, ma solo di ciò che conta davvero.
        Con soli 15 euro al mese, ottieni 100 minuti di chiamate e 50 SMS, perfetti per restare in contatto con chi ti è più caro,
        senza preoccuparti di extra inutili. Attivabile con una spesa iniziale di soli 10 euro, 'basic talk' è la soluzione ideale per chi cerca un
        piano mobile semplice e affidabile. Con 1GB di dati inclusi, potrai navigare in tutta tranquillità, restando sempre connesso per le tue necessità quotidiane.
        Ideale per i privati che vogliono un piano economico senza sorprese, 'basic talk' ti offre la libertà di gestire le tue comunicazioni come preferisci.
        Dì addio ai costi esorbitanti e scegli la semplicità: con 'basic talk', hai tutto ciò di cui hai bisogno, a un prezzo che ti farà sorridere
        """,
        metadata={
            "id": "o1",
            "tipo": "mobile",
            "utenza": "privati",
            "nome": "basic talk",
        },
    ),
    Document(
        page_content="""
        Se cerchi di più dal tuo piano mobile, 'standard connect' è ciò che fa per te.
        Con 25 euro al mese, puoi dire addio alle limitazioni: avrai a disposizione 5GB di dati per navigare liberamente,
        300 minuti di chiamate e SMS illimitati per tenerti sempre connesso con il mondo.
        Il piano perfetto per chi ama comunicare senza interruzioni e ha bisogno di maggiore flessibilità,
        'standard connect' ti offre tutto ciò che serve per restare aggiornato, ovunque tu sia.
        Attiva il piano oggi stesso con una spesa iniziale di soli 15 euro e goditi il perfetto equilibrio tra qualità e convenienza.
        Con 'standard connect', resti in contatto senza compromessi, perché la connessione non dovrebbe mai essere un ostacolo.
        Questa offerta è studiata per i privati che vogliono di più, senza dover spendere una fortuna.
        """,
        metadata={
            "id": "o2",
            "tipo": "mobile",
            "utenza": "privati",
            "nome": "standard connect",
        },
    ),
    Document(
        page_content="""
        Sei stanco di dover tenere d'occhio i tuoi consumi? 'Unlimited plus' è la soluzione definitiva per una libertà totale.
        Con soli 40 euro al mese, puoi finalmente dire addio a ogni limite: minuti, SMS e persino dati illimitati.
        Sì, hai letto bene, tutto illimitato! Naviga senza pensieri, chiama quanto vuoi e invia SMS senza freni, ovunque ti trovi.
        Questo piano è pensato per chi ha bisogno del massimo senza compromessi: se sei sempre in movimento, 
        lavori online o semplicemente non vuoi preoccuparti delle soglie mensili, 'unlimited plus' è ciò che fa per te.
        Con un costo di attivazione di soli 20 euro, ti metti al riparo da ogni sorpresa e inizi subito a vivere l'esperienza
        di una connessione senza confini. Dedicato ai privati, questo piano è perfetto per chi ha uno stile di vita
        digitale e non vuole interruzioni.
        """,
        metadata={
            "id": "o3",
            "tipo": "mobile",
            "utenza": "privati",
            "nome": "unlimited plus",
        },
    ),
    Document(
        page_content="""
        La famiglia è importante, e anche il tuo piano mobile dovrebbe esserlo. Con 'family saver', hai finalmente un'offerta che pensa a tutti.
        Con soli 60 euro al mese, avrai a disposizione 50GB di dati da condividere tra tutti i membri della tua famiglia,
        1000 minuti di chiamate e 500 SMS. Un solo piano che soddisfa le esigenze di tutti, permettendo a te e ai tuoi cari di rimanere connessi,
        senza dover gestire più conti o piani separati. Ideale per i privati, 'family saver' è la scelta intelligente per le famiglie moderne
        che vogliono risparmiare senza rinunciare alla qualità. Attiva subito il piano con un contributo iniziale di soli 25 euro e inizia
        a godere di un piano condiviso che pensa a tutta la famiglia. Con 'family saver', la connessione non è mai stata così semplice e conveniente.
        """,
        metadata={
            "id": "o4",
            "tipo": "mobile",
            "utenza": "privati",
            "nome": "family saver",
        },
    ),
    Document(
        page_content="""
        Per i professionisti e le aziende, la connettività non è un lusso, ma una necessità.
        'Business pro' è l'offerta premium che ti garantisce un servizio impeccabile e l'affidabilità che meriti.
        Con 75 euro al mese, ottieni dati e minuti illimitati, oltre a SMS senza limiti. Il tutto supportato da un servizio clienti premium
        e funzionalità aggiuntive per chi fa del proprio lavoro una priorità. Con un contributo di attivazione di soli 30 euro,
        il tuo piano sarà pronto per darti tutto ciò di cui hai bisogno, senza compromessi. Ideale per le aziende e i professionisti,
        'business pro' è la scelta giusta per chi necessita di un piano affidabile, flessibile e sempre pronto a rispondere alle esigenze del mondo
        del lavoro. Con 'business pro', il successo è solo una questione di connettività.
        """,
        metadata={
            "id": "o5",
            "tipo": "mobile",
            "utenza": "business",
            "nome": "business pro",
        },
    ),
    Document(
        page_content="""
        Se viaggi spesso per lavoro, sai quanto è importante avere un piano che ti segua ovunque tu vada.
        'Traveler's choice' è pensato per i professionisti che si spostano regolarmente e non vogliono rinunciare a un servizio di qualità
        anche all'estero. Con 50 euro al mese, avrai 10GB di dati, 500 minuti di chiamate e SMS illimitati per rimanere sempre connesso,
        sia in patria che all'estero. Attiva il piano con un contributo di 20 euro e non dovrai più preoccuparti delle tariffe roaming.
        'Traveler's choice' è la scelta perfetta per i viaggiatori d'affari che necessitano di un piano affidabile e flessibile, ovunque
        si trovino. Scegli 'Traveler's choice' e scopri la libertà di una connessione globale.
        """,
        metadata={
            "id": "o6",
            "tipo": "mobile",
            "utenza": "business",
            "nome": "traveler's choice",
        },
    ),
    Document(
        page_content="""
        Vuoi portare la potenza della fibra nella tua casa senza spendere una fortuna?
        'Fiber basic' è l'offerta che fa per te. Con soli 30 euro al mese, puoi avere una connessione stabile e veloce per
        la tua linea fissa, con 100GB di dati inclusi. Ideale per i privati, 'fiber basic' è la scelta perfetta per chi
        cerca un'opzione economica senza sacrificare la qualità della connessione. Con un costo di attivazione di 50 euro,
        potrai subito iniziare a navigare alla velocità della luce. Non importa se lavori da casa, guardi video in streaming o
        giochi online, 'fiber basic' ti offre tutto ciò di cui hai bisogno per restare connesso. Porta il futuro della connettività a
        casa tua con 'fiber basic'.
        """,
        metadata={
            "id": "o7",
            "tipo": "fibra",
            "utenza": "privati",
            "nome": "fiber basic",
        },
    ),
    Document(
        page_content="""
        Per chi cerca il massimo dalla connessione fissa, 'fiber premium' è l'offerta che fa per te.
        Con 60 euro al mese, ottieni 200GB di dati, perfetti per chi ha bisogno di una connessione stabile e ultra-veloce.
        Ideale per i privati che lavorano da casa o hanno una famiglia numerosa, 'fiber premium' ti garantisce prestazioni di alto 
        livello senza interruzioni. Attiva subito il piano con un contributo di 75 euro e goditi la libertà di una connessione affidabile e potente.
        'Fiber premium' è la soluzione per chi non accetta compromessi e vuole solo il meglio per la propria casa. Naviga, gioca, guarda film in 
        streaming senza mai preoccuparti della connessione.
        """,
        metadata={
            "id": "o8",
            "tipo": "fibra",
            "utenza": "privati",
            "nome": "fiber premium",
        },
    ),
    Document(
        page_content="""
        Se hai un'azienda, sai quanto è fondamentale avere una connessione internet affidabile e veloce.
        'Fiber business' ti offre esattamente questo, con 500GB di dati a disposizione per soddisfare le esigenze della tua impresa.
        Con un costo mensile di 90 euro e un contributo di attivazione di 100 euro, potrai avere una connessione stabile, sicura e veloce,
        perfetta per tutte le attività online della tua azienda. 'Fiber business' è pensata per le piccole e medie imprese che necessitano di
        una connessione performante per restare competitive. Non perdere altro tempo: attiva 'fiber business' e porta la tua azienda al livello
        successivo con la potenza della fibra.
        """,
        metadata={
            "id": "o9",
            "tipo": "fibra",
            "utenza": "business",
            "nome": "fiber business",
        },
    ),
]


# Lista degli utenti
users = [
    "Mario Rossi",
    "Giulia Bianchi",
    "Luca Verdi",
    "Francesca Gialli",
    "Alessandro Neri",
    "Sofia Blu",
]


query = """
CREATE
(u1:Utente { id:'u1', nome:'mario', cognome:'rossi', codiceFiscale:'MRORSS80A01H501Z', email:'mario.rossi@example.com', utenzaFissa:'0612345678', utenzaMobile:'3887654856' }),
(u2:Utente { id:'u2', nome:'giulia', cognome:'bianchi', codiceFiscale:'BNCGLL85P41H501S', email:'giulia.bianchi@example.com', utenzaFissa:'0645214785', utenzaMobile:'3282677458' }),
(u3:Utente { id:'u3', nome:'luca', cognome:'verdi', codiceFiscale:'VRDLCU85M01H501X', email:'luca.verdi@example.com', utenzaFissa: null , utenzaMobile:'+39 3884512745' }),
(u4:Utente { id:'u4', nome:'francesca', cognome:'gialli', codiceFiscale:'GLLFNC75P41H501Y', email:'francesca.gialli@example.com', utenzaFissa:'0612345679', utenzaMobile:'3285478956' }),
(u5:Utente { id:'u5', nome:'alessandro', cognome:'neri', codiceFiscale:'NRLSSN90M01H501Z', email:'alessandro.neri@example.com', utenzaFissa:'0612345681', utenzaMobile: null }),
(u6:Utente { id:'u6', nome:'sofia', cognome:'blu', codiceFiscale:'BLUSOF90L01H501B', email:'sofia.blu@example.com', utenzaFissa: null , utenzaMobile:'3884578165' }),

(o1:Offerta { id:'o1', tipo:'mobile', nome:'basic talk', descrizione:'piano base con chiamate e sms essenziali.', costoMensile:'15 €', costoAttivazione:'10 €', dati:'1GB', minuti:100, sms:50 }),
(o2:Offerta { id:'o2', tipo:'mobile', nome:'standard connect', descrizione:'piano intermedio con più dati e sms illimitati.', costoMensile:'25€', costoAttivazione:'15€', dati:'5GB', minuti:300, sms:'illimitati' }),
(o3:Offerta { id:'o3', tipo:'mobile', nome:'unlimited plus', descrizione:'chiamate, sms e dati illimitati.', costoMensile:'40€', costoAttivazione:'20€', dati:'20GB', minuti:'illimitati', sms:'illimitati' }),
(o4:Offerta { id:'o4', tipo:'mobile', nome:'family saver', descrizione:'piano famiglia con dati e minuti condivisi.', costoMensile:'60€', costoAttivazione:'25€', dati:'50GB', minuti:1000, sms:500 }),
(o5:Offerta { id:'o5', tipo:'mobile', nome:'business pro', descrizione:'piano aziendale con servizi premium e supporto.', costoMensile:'75€', costoAttivazione:'30€', dati:'illimitato', minuti: 'illimitati', sms:'illimitati' }),
(o6:Offerta { id:'o6', tipo:'mobile', nome:"traveler\'s choice", descrizione:"piano per chi viaggia spesso all\'estero.", costoMensile:'50€', costoAttivazione:'20€', dati:'10GB', minuti: 500, sms: 'illimitati' }),
(o7:Offerta { id:'o7', tipo:'fibra', nome:'fiber basic', descrizione:'servizio fibra base per linea fissa.', costoMensile:'30 €', costoAttivazione:'50 €', dati:'100 GB' }),
(o8:Offerta { id:'o8', tipo:'fibra', nome:'fiber premium', descrizione:'servizio fibra premium per linea fissa.', costoMensile:'60€', costoAttivazione:'75€', dati:'200 GB' }),
(o9:Offerta { id:'o9', tipo:'fibra', nome:'fiber business', descrizione:'servizio fibra per uso aziendale.', costoMensile:'90€', costoAttivazione:'100€', dati:'500GB' }),

(c1:Contratto {id:'c1', utenteId:'u1', durata:'24 mesi', file:'https: //example.com/contratti/c1.pdf'}),
(c2:Contratto {id:'c2', utenteId:'u2', durata:'12 mesi', file:'https: //example.com/contratti/c2.pdf'}),
(c3:Contratto {id:'c3', utenteId:'u3', durata:'36 mesi', file:'https: //example.com/contratti/c3.pdf'}),
(c4:Contratto {id:'c4', utenteId:'u4', durata:'18 mesi', file:'https: //example.com/contratti/c4.pdf'}),
(c5:Contratto {id:'c5', utenteId:'u5', durata:'12 mesi', file:'https: //example.com/contratti/c5.pdf'}),
(c6:Contratto {id:'c6', utenteId:'u6', durata:'24 mesi', file:'https: //example.com/contratti/c6.pdf'}),
(c7:Contratto {id:'c7', utenteId:'u1', durata:'12 mesi', file:'https: //example.com/contratti/c7.pdf'}),
(c8:Contratto {id:'c8', utenteId:'u2', durata:'24 mesi', file:'https: //example.com/contratti/c8.pdf'}),
(c9:Contratto {id:'c9', utenteId:'u4', durata:'24 mesi', file:'https: //example.com/contratti/c9.pdf'}),

(u1)-[:HA_SOTTOSCRITTO { dataSottoscrizione:'2024-01-01' }]->(c1)-[:RELATIVO_A]->(o8)<-[:HA_ATTIVATO { dataInizio:'2024-01-01', dataFine:'2025-01-01', residuoDati: '100GB' }]-(u1),
(u1)-[:HA_SOTTOSCRITTO { dataSottoscrizione:'2024-07-01' }]->(c7)-[:RELATIVO_A]->(o3)<-[:HA_ATTIVATO { dataInizio:'2024-07-01', dataFine:'2025-07-01', residuoDati: '16GB', residuoMinuti: 'illimitati', residuoSMS: 'illimitati' }]-(u1),
(u2)-[:HA_SOTTOSCRITTO { dataSottoscrizione:'2024-02-01' }]->(c2)-[:RELATIVO_A]->(o1)<-[:HA_ATTIVATO { dataInizio:'2024-02-01', dataFine:'2025-02-01', residuoDati: '1GB', residuoMinuti: 66, residuoSMS: 41 }]-(u2),
(u2)-[:HA_SOTTOSCRITTO { dataSottoscrizione:'2024-08-01' }]->(c8)-[:RELATIVO_A]->(o7)<-[:HA_ATTIVATO { dataInizio:'2024-08-01', dataFine:'2025-08-01', residuoDati: '21GB' }]-(u2),
(u3)-[:HA_SOTTOSCRITTO { dataSottoscrizione:'2024-03-01' }]->(c3)-[:RELATIVO_A]->(o4)<-[:HA_ATTIVATO { dataInizio:'2024-03-01', dataFine:'2026-03-01', residuoDati: '38GB', residuoMinuti: 731, residuoSMS: 160 }]-(u3),
(u4)-[:HA_SOTTOSCRITTO { dataSottoscrizione:'2024-04-01' }]->(c4)-[:RELATIVO_A]->(o5)<-[:HA_ATTIVATO { dataInizio:'2024-04-01', dataFine:'2025-04-01', residuoDati: 'illimitati', residuoMinuti: 'illimitati', residuoSMS: 'illimitati' }]-(u4),
(u4)-[:HA_SOTTOSCRITTO { dataSottoscrizione:'2024-05-01' }]->(c9)-[:RELATIVO_A]->(o6)<-[:HA_ATTIVATO { dataInizio:'2024-05-01', dataFine:'2025-05-01', residuoDati: '4GB', residuoMinuti: 100, residuoSMS: 'illimitati' }]-(u4),
(u5)-[:HA_SOTTOSCRITTO { dataSottoscrizione:'2024-05-01' }]->(c5)-[:RELATIVO_A]->(o9)<-[:HA_ATTIVATO { dataInizio:'2024-05-01', dataFine:'2026-05-01', residuoDati: '3800GB' }]-(u5),
(u6)-[:HA_SOTTOSCRITTO { dataSottoscrizione:'2024-06-01' }]->(c6)-[:RELATIVO_A]->(o2)<-[:HA_ATTIVATO { dataInizio:'2024-06-01', dataFine:'2025-06-01', residuoDati: '2GB', residuoMinuti: 180, residuoSMS: 'illimitati' }]-(u6)
"""


slides = r"""
    # Retrieval Augmented Generation
    `tecnica per aumentare la conoscenza di un LLM con dati aggiuntivi`
    ---
    ## Agentic RAG
    <!-- .slide: data-background-color="#FFFFFF" -->
    ![](https://miro.medium.com/v2/resize:fit:1400/0*3O1QAj_62FzWydQj.png)
    ---
    ## Re-Act Architecture
    `paradigma che combina il ragionamento e l'azione con i LLM, richiedendo ai modelli di generare tracce di ragionamento verbale e azioni per un'attività`
    ---
    ## Tech Stack
    `python based - full stack`

    \[[Langchain](https://python.langchain.com/docs/introduction/)\] \[[Neo4j](https://neo4j.com/labs/genai-ecosystem/langchain/)\] \[[Qdrant](https://qdrant.tech/documentation/frameworks/langchain/)\] \[[mockAPI](https://mockapi.io/)\] \[[Streamlit](https://streamlit.io/generative-ai)\]

"""
slide_caption = [
    "I LLM possono ragionare e generare risposte su innumerevoli argomenti, ma la loro conoscenza è limitata ai dati pubblici osservati fino al momento specifico del loro addestramento. Per creare applicazioni IA in grado di rispondere su dataset proprietari o rispetto ad informazioni aggiornate/presenti a dopo la data limite di un modello, bisogna aumentare la loro conoscenza integrando nuove fonti informative.",
    "Gli agenti sono sistemi che utilizzano un LLM come motore di ragionamento per determinare quali azioni intraprendere e quali dovrebbero essere gli input per tali azioni. I risultati di tali azioni possono quindi essere reimmessi nell'agente che determina se sono necessarie ulteriori azioni o se è possibile terminarle.",
    """
    - Il modello "riflette" su quale passo compiere in risposta a un input
    - Successivamente sceglie un'azione tra gli strumenti disponibili (oppure sceglie di rispondere direttamente)
    - Il modello genera gli argomenti per lo strumento
    - Il runtime dell'agente (esecutore) richiama lo strumento con gli argomenti generati
    - L'esecutore restituisce al modello i risultati della chiamata allo strumento come un'osservazione
    """,
    """
    - `Langchain` è utilizzato per orchestrare l'agente ReAct
    - `Neo4J`, tramite il query language `CYPHER`, permette di navigare nei grafi per recuperare informazioni strutturate
    - `Qdrant` è un motore di ricerca vettoriale, utilizzato qui per la gestione degli embedding semantici.
    - `mockAPI` fornisce endpoint di test che simulano risposte da fonti di dati esterne o servizi.
    - `Streamlit` implementa l'interfaccia utente
    """,
    "",
]
