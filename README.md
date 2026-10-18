    # ⚓ OSINT-Driven Corporate Executive Spear Phishing Sandbox Project

    ## ⚠️ Legal & Ethical Disclaimer
    **CRITICAL NOTICE:** This repository is constructed strictly for academic review, structural demonstration, and educational grading metrics. All domains, corporate identities, email paths, and user activities detailed within this portfolio are 100% fictional or explicitly owned by the authors. No actual Personally Identifiable Information (PII) was targeted, gathered, or processed, ensuring total structural compliance with local privacy frameworks (including GDPR, CCPA) and ethical data gathering policies.

    ---

    ## 📈 System Architecture & Intelligence Pipeline
    This mini-project demonstrates the standard 4-stage offensive reconnaissance workflow an external threat actor uses to profile corporate executives, using a completely controlled mockup environment hosted right here on GitHub Pages.

    ```text
    [1. Target Selection]                [2. Corporate Mapping]
    Host Sandbox Site Built  ---------->  Infrastructure Analytics
    (GitHub Corporate Portal)             (theHarvester / DNSRecon)
                                                        │
                                                        ▼
    [4. Attack Vector Simulation]         [3. Personal Profiling]
    Tailored Psychological Bait <---------- Digital Footprint Crawl
    (Targeted Mock Spear-Phish)              (ExifTool / Sherlock / Dorks)
    ```

    ---

    ## 🛠️ Deep-Dive 5-Tool Demonstration Breakdown

    ### 1. theHarvester (Asset Discovery)
    * **Objective:** Establish corporate email naming structures and locate publicly visible endpoints.
    * **Command Executed:** `theHarvester -d yourusername.github.io -l 200 -b google,bing`
    * **Findings:** Identified administrative contact frameworks and confirmed target organizational handles: `janesmith@apex-global.local` and `admin@apex-global.local`.

    ### 2. ExifTool (Document Metadata Leakage)
    * **Objective:** Extract structural data parameters from public document file downloads.
    * **Command Executed:** `exiftool assets/mock_invoice.pdf`
    * **Findings:** Document properties exposed that the document author is **Jane Smith** and exposed an internal network share path directory: `//AGL-NAS-01/Volume1/Users/jsmith/Docs/`.

    ### 3. DNSRecon (Infrastructure Verification)
    * **Objective:** Map structural mail servers without communicating with live enterprise endpoints directly.
    * **Command Executed:** `dnsrecon -d github.io -t std`
    * **Findings:** Authoritative pointers verify underlying infrastructure layouts. In a real-world scenario, this allows an attacker to know whether to build a duplicate Office 365 or Google Workspace landing page to catch credentials.

    ### 4. Sherlock (Social Media Intelligence / SOCMINT)
    * **Objective:** Pivot from professional channels to personal spaces using cross-platform username correlation.
    * **Command Executed:** `python3 sherlock.py janesmith_apex`
    * **Findings:** Isolated active open profile accounts. Cross-referencing forum trails explicitly confirms high personal interest and attendance plans for the upcoming **Annual Regional Charity Golf Invitational**.

    ### 5. Advanced Google Dorking (Target Index Filtering)
    * **Objective:** Isolate deep file architectures within major public indexing engines.
    * **Query Used:** `site:yourusername.github.io/apex-global-logistics/ filetype:pdf`
    * **Findings:** Proved that targeted indexing bypasses frontend public relations barriers to quickly scrape backend functional corporate reports like invoices or structural flowcharts.

    ---

    ## 🎣 Synthesis: OSINT-Driven Mock Spear-Phishing Attack Vector
    By overlaying our collected datasets, a highly convincing, targeted communication bait is synthesized:

    * **Target Vector:** `janesmith@apex-global.local` (From **theHarvester**)
    * **Delivery Spoof Path:** Mimicking the Office 365 administrative structure (From **DNSRecon**)
    * **Psychological Hook:** The Annual Regional Charity Golf Invitational (From **Sherlock**)
    * **Technical Anchor Vector:** Reference to file path directory structure layouts (From **ExifTool**)

    ### 📧 Mock Blueprint Layout
    > **Subject:** URGENT: Updates Regarding Registration for the Annual Regional Charity Golf Invitational
    >
    > **Body:**  
    > Hello Jane,  
    >   
    > We noticed an anomaly regarding the administrative files submitted for Apex Global Logistics' upcoming title sponsorship package at the charity event. It looks like the file settings tying into directory path `//AGL-NAS-01/Volume1/Users/jsmith/Docs/` did not sync correctly with our portal database.  
    >   
    > To ensure your executive seating and event registration remain confirmed for next month's tournament, please re-verify your submission settings by logging into the coordinator portal link below:  
    >   
    > `http://secure-verify.local`  
    >   
    > Best Regards,  
    > **Event Coordination Committee**

    ---

    ## 🛡️ Executive Defenses & Countermeasures
    To protect corporate leaders from these exact methodologies, enterprises must implement three critical pillars:
    1. **Strict Metadata Scrubbing Policies:** Enforce automated gateway scrubbing scripts that completely wipe EXIF metadata tags from all internal files before they are uploaded to the public internet.
    2. **Social Engineering Resilience Training:** Move away from generic phishing tests and implement context-aware simulations that explicitly show executives how their personal hobbies (like golf, running, or charity work) can be turned into bait.
    3. **Robust External Attack Surface Management (EASM):** Run continuous Google Dorking sweeps and username tracking audits to find out what information is exposed *before* adversaries can map it out.
