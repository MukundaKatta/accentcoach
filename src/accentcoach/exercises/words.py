"""Problem word database with 200+ commonly mispronounced words."""

from __future__ import annotations

from accentcoach.models import WordPronunciation


class ProblemWordDatabase:
    """Database of 200+ commonly mispronounced English words."""

    # Each entry: (word, IPA, syllable_count, common_errors)
    WORDS: list[tuple[str, str, int, list[str]]] = [
        # --- A ---
        ("acai", "/\u0259\u02c8sa\u026a.i\u02d0/", 3, ["ah-KAI"]),
        ("almond", "/\u02c8\u0251\u02d0m\u0259nd/", 2, ["AL-mond"]),
        ("anemone", "/\u0259\u02c8nem\u0259ni\u02d0/", 4, ["ah-NEH-moan"]),
        ("anonymous", "/\u0259\u02c8n\u0252n\u026am\u0259s/", 4, []),
        ("antarctic", "/\u00e6n\u02c8t\u0251\u02d0kt\u026ak/", 4, ["ant-AR-tic"]),
        ("ask", "/\u0251\u02d0sk/", 1, ["axe"]),
        ("athlete", "/\u02c8\u00e6\u03b8li\u02d0t/", 2, ["ATH-a-lete"]),
        # --- B ---
        ("ballet", "/b\u00e6\u02c8le\u026a/", 2, ["BAL-let"]),
        ("breakfast", "/\u02c8b\u0279ek.f\u0259st/", 2, ["BREEK-fast"]),
        ("bury", "/\u02c8be\u0279i\u02d0/", 2, ["BUR-ee"]),
        ("business", "/\u02c8b\u026azn\u0259s/", 2, ["BIZ-ee-ness"]),
        # --- C ---
        ("cache", "/k\u00e6\u0283/", 1, ["kah-SHAY"]),
        ("candidate", "/\u02c8k\u00e6nd\u026ade\u026at/", 3, ["CAN-uh-date"]),
        ("chaos", "/\u02c8ke\u026a\u0252s/", 2, ["CHAH-os"]),
        ("choir", "/kwa\u026a\u0259/", 2, ["CHOY-er"]),
        ("colonel", "/\u02c8k\u025c\u02d0n\u0259l/", 2, ["koh-LON-el"]),
        ("comfortable", "/\u02c8k\u028cmf.t\u0259.b\u0259l/", 3, ["com-FOR-table"]),
        ("coup", "/ku\u02d0/", 1, ["koop"]),
        ("cupboard", "/\u02c8k\u028cb\u0259d/", 2, ["CUP-board"]),
        # --- D ---
        ("debris", "/d\u0259\u02c8b\u0279i\u02d0/", 2, ["DEB-riss"]),
        ("definitely", "/\u02c8def\u026an\u026atli\u02d0/", 4, ["DEF-in-ATE-lee"]),
        ("determine", "/d\u026a\u02c8t\u025c\u02d0m\u026an/", 3, []),
        ("develop", "/d\u026a\u02c8vel\u0259p/", 3, []),
        ("diamond", "/\u02c8da\u026a\u0259m\u0259nd/", 2, ["DI-a-mond"]),
        # --- E ---
        ("environment", "/\u026an\u02c8va\u026a\u0259\u0279\u0259nm\u0259nt/", 4, ["en-VI-ern-ment"]),
        ("epitome", "/\u026a\u02c8p\u026at\u0259mi\u02d0/", 4, ["EP-ih-toam"]),
        ("espresso", "/e\u02c8sp\u0279es\u0259\u028a/", 3, ["EX-presso"]),
        ("etcetera", "/et\u02c8set\u0259\u0279\u0259/", 4, ["ek-SET-era"]),
        ("et cetera", "/et\u02c8set\u0259\u0279\u0259/", 4, ["ek-SET-era"]),
        ("executive", "/\u026a\u0261\u02c8zekj\u028at\u026av/", 4, []),
        # --- F ---
        ("facade", "/f\u0259\u02c8s\u0251\u02d0d/", 2, ["FAH-kade"]),
        ("february", "/\u02c8feb\u0279u\u02d0e\u0279i\u02d0/", 4, ["FEB-yoo-airy"]),
        ("figure", "/\u02c8f\u026a\u0261j\u0259/", 2, ["FIG-er"]),
        ("flour", "/\u02c8fla\u028a\u0259/", 2, ["flor"]),
        ("foliage", "/\u02c8f\u0259\u028ali\u02d0\u026ad\u0292/", 3, ["FOIL-idge"]),
        # --- G ---
        ("genre", "/\u02c8\u0292\u0251\u02d0n\u0279\u0259/", 2, ["JEN-er"]),
        ("genuine", "/\u02c8d\u0292enj\u028a\u026an/", 3, ["JEN-yoo-wine"]),
        ("gif", "/d\u0292\u026af/", 1, ["ghif"]),
        ("gourmet", "/\u0261\u028a\u0259\u02c8me\u026a/", 2, ["GOR-met"]),
        ("government", "/\u02c8\u0261\u028cv\u0259nm\u0259nt/", 3, ["GUV-er-ment"]),
        # --- H ---
        ("height", "/ha\u026at/", 1, ["heighth"]),
        ("herb", "/\u025c\u02d0b/", 1, ["h-erb"]),
        ("hierarchy", "/\u02c8ha\u026a\u0259\u0279\u0251\u02d0ki\u02d0/", 4, ["HI-ar-kee"]),
        ("hyperbole", "/ha\u026a\u02c8p\u025c\u02d0b\u0259li\u02d0/", 4, ["HY-per-bowl"]),
        # --- I ---
        ("ignore", "/\u026a\u0261\u02c8n\u0254\u02d0/", 2, []),
        ("important", "/\u026am\u02c8p\u0254\u02d0t\u0259nt/", 3, []),
        ("interesting", "/\u02c8\u026ant\u0279\u0259st\u026a\u014b/", 3, ["IN-ter-EST-ing"]),
        ("isthmus", "/\u02c8\u026asm\u0259s/", 2, ["IS-th-mus"]),
        ("itinerary", "/a\u026a\u02c8t\u026an\u0259\u0279e\u0279i\u02d0/", 5, ["eye-TIN-airy"]),
        # --- J-K ---
        ("jewelry", "/\u02c8d\u0292u\u02d0\u0259l\u0279i\u02d0/", 3, ["JOO-la-ree"]),
        ("kernel", "/\u02c8k\u025c\u02d0n\u0259l/", 2, []),
        ("knowledge", "/\u02c8n\u0252l\u026ad\u0292/", 2, ["kuh-NOW-ledge"]),
        # --- L ---
        ("laboratory", "/l\u0259\u02c8b\u0252\u0279\u0259t\u0279i\u02d0/", 5, ["LAB-ra-tory"]),
        ("language", "/\u02c8l\u00e6\u014b\u0261w\u026ad\u0292/", 2, []),
        ("library", "/\u02c8la\u026ab\u0279e\u0279i\u02d0/", 3, ["LIE-berry"]),
        ("lingerie", "/\u02c8l\u00e6n\u0292\u0259\u0279e\u026a/", 3, ["LIN-juh-ree"]),
        ("lieutenant", "/lu\u02d0\u02c8ten\u0259nt/", 3, []),
        # --- M ---
        ("meme", "/mi\u02d0m/", 1, ["may-may"]),
        ("mischievous", "/\u02c8m\u026ast\u0283\u026av\u0259s/", 3, ["mis-CHEE-vee-us"]),
        ("miscellaneous", "/\u02ccm\u026as\u0259\u02c8le\u026ani\u02d0\u0259s/", 5, []),
        ("mortgage", "/\u02c8m\u0254\u02d0\u0261\u026ad\u0292/", 2, ["MORT-gage"]),
        ("muscle", "/\u02c8m\u028cs\u0259l/", 2, []),
        ("museum", "/mju\u02d0\u02c8zi\u02d0\u0259m/", 3, []),
        # --- N ---
        ("naive", "/na\u026a\u02c8i\u02d0v/", 2, []),
        ("niche", "/ni\u02d0\u0283/", 1, ["nitch"]),
        ("nuclear", "/\u02c8nju\u02d0kli\u02d0\u0259/", 3, ["NOO-kyoo-lar"]),
        # --- O ---
        ("often", "/\u02c8\u0252fn\u0329/", 2, ["OFF-ten"]),
        ("onomatopoeia", "/\u02cc\u0252n\u0259\u02ccm\u00e6t\u0259\u02c8pi\u02d0\u0259/", 6, []),
        ("orchestra", "/\u02c8\u0254\u02d0k\u026ast\u0279\u0259/", 3, []),
        # --- P ---
        ("particular", "/p\u0259\u02c8t\u026akj\u028al\u0259/", 4, []),
        ("picture", "/\u02c8p\u026akt\u0283\u0259/", 2, []),
        ("pizza", "/\u02c8pi\u02d0ts\u0259/", 2, []),
        ("plateau", "/pl\u00e6\u02c8t\u0259\u028a/", 2, ["PLAT-ee-oh"]),
        ("poem", "/\u02c8p\u0259\u028a\u026am/", 2, ["poim"]),
        ("prerogative", "/p\u0279\u026a\u02c8\u0279\u0252\u0261\u0259t\u026av/", 4, ["per-OG-a-tive"]),
        ("probably", "/\u02c8p\u0279\u0252b\u0259bli\u02d0/", 3, ["PROB-lee"]),
        ("pronunciation", "/p\u0279\u0259\u02ccn\u028cns\u026a\u02c8e\u026a\u0283\u0259n/", 5, ["pro-NOUN-ciation"]),
        ("pseudo", "/\u02c8sju\u02d0d\u0259\u028a/", 2, []),
        # --- Q ---
        ("queue", "/kju\u02d0/", 1, ["KWAY-way"]),
        ("quinoa", "/\u02c8ki\u02d0nw\u0251\u02d0/", 2, ["KWIN-oh-ah"]),
        # --- R ---
        ("receipt", "/\u0279\u026a\u02c8si\u02d0t/", 2, []),
        ("recipe", "/\u02c8\u0279es\u026api\u02d0/", 3, ["reh-SIPE"]),
        ("recognize", "/\u02c8\u0279ek\u0259\u0261na\u026az/", 3, []),
        ("regime", "/\u0279e\u026a\u02c8\u0292i\u02d0m/", 2, []),
        ("rendezvous", "/\u02c8\u0279\u0252nde\u026avu\u02d0/", 3, []),
        ("restaurant", "/\u02c8\u0279est\u0259\u0279\u0252nt/", 3, ["REST-er-awnt"]),
        # --- S ---
        ("sacrilegious", "/\u02ccs\u00e6k\u0279\u026a\u02c8l\u026ad\u0292\u0259s/", 4, ["SAC-ri-LIDGE-us"]),
        ("salmon", "/\u02c8s\u00e6m\u0259n/", 2, ["SAL-mon"]),
        ("sandwich", "/\u02c8s\u00e6nw\u026at\u0283/", 2, []),
        ("schedule", "/\u02c8\u0283edju\u02d0l/", 2, []),
        ("scissors", "/\u02c8s\u026az\u0259z/", 2, []),
        ("specific", "/sp\u0259\u02c8s\u026af\u026ak/", 3, ["pa-SIFIC"]),
        ("stomach", "/\u02c8st\u028cm\u0259k/", 2, []),
        ("subtle", "/\u02c8s\u028ct\u0259l/", 2, ["SUB-tle"]),
        ("suite", "/swi\u02d0t/", 1, ["soot"]),
        ("supposedly", "/s\u0259\u02c8p\u0259\u028az\u026adli\u02d0/", 4, ["suh-POSE-ably"]),
        # --- T ---
        ("temperature", "/\u02c8temp\u0259\u0279\u0259t\u0283\u0259/", 4, ["TEMP-a-chure"]),
        ("thesaurus", "/\u03b8\u026a\u02c8s\u0254\u02d0\u0279\u0259s/", 3, []),
        ("thoroughly", "/\u02c8\u03b8\u028c\u0279\u0259li\u02d0/", 3, []),
        ("toward", "/t\u0259\u02c8w\u0254\u02d0d/", 2, []),
        ("triathlon", "/t\u0279a\u026a\u02c8\u00e6\u03b8l\u0252n/", 3, ["try-ATH-a-lon"]),
        ("turmeric", "/\u02c8t\u025c\u02d0m\u0259\u0279\u026ak/", 3, ["TUR-muh-rick"]),
        # --- U-V ---
        ("utensil", "/ju\u02d0\u02c8tens\u0259l/", 3, []),
        ("vehicle", "/\u02c8vi\u02d0\u026ak\u0259l/", 3, ["veh-HICK-le"]),
        ("vegetable", "/\u02c8ved\u0292t\u0259b\u0259l/", 3, ["VEG-eh-table"]),
        ("vulnerable", "/\u02c8v\u028cln\u0259\u0279\u0259b\u0259l/", 4, []),
        # --- W ---
        ("wednesday", "/\u02c8wenzde\u026a/", 2, ["WED-ness-day"]),
        ("worcestershire", "/\u02c8w\u028ast\u0259\u0283\u0259/", 3, ["WOR-cester-shire"]),
        # --- X-Z ---
        ("xenophobia", "/\u02cczen\u0259\u02c8f\u0259\u028abi\u02d0\u0259/", 5, []),
        ("yacht", "/j\u0252t/", 1, ["yatcht"]),
        ("zealous", "/\u02c8zel\u0259s/", 2, []),
        # --- More commonly mispronounced ---
        ("accessory", "/\u0259k\u02c8ses\u0259\u0279i\u02d0/", 4, []),
        ("archive", "/\u02c8\u0251\u02d0ka\u026av/", 2, []),
        ("asterisk", "/\u02c8\u00e6st\u0259\u0279\u026ask/", 3, ["AS-ter-ix"]),
        ("awry", "/\u0259\u02c8\u0279a\u026a/", 2, ["AW-ree"]),
        ("blatant", "/\u02c8ble\u026at\u0259nt/", 2, []),
        ("bouquet", "/bu\u02d0\u02c8ke\u026a/", 2, []),
        ("brochure", "/b\u0279\u0259\u028a\u02c8\u0283\u028a\u0259/", 2, []),
        ("caramel", "/\u02c8k\u00e6\u0279\u0259mel/", 3, []),
        ("catastrophe", "/k\u0259\u02c8t\u00e6st\u0279\u0259fi\u02d0/", 4, []),
        ("chimera", "/ka\u026a\u02c8m\u026a\u0259\u0279\u0259/", 3, []),
        ("cinnamon", "/\u02c8s\u026an\u0259m\u0259n/", 3, []),
        ("clandestine", "/kl\u00e6n\u02c8dest\u026an/", 3, []),
        ("clothes", "/kl\u0259\u028a\u00f0z/", 1, ["CLOZE"]),
        ("cocoa", "/\u02c8k\u0259\u028ak\u0259\u028a/", 2, []),
        ("conundrum", "/k\u0259\u02c8n\u028cnd\u0279\u0259m/", 3, []),
        ("coupon", "/\u02c8ku\u02d0p\u0252n/", 2, []),
        ("croissant", "/kw\u00e6\u02c8s\u0252\u014b/", 2, []),
        ("cuisine", "/kw\u026a\u02c8zi\u02d0n/", 2, []),
        ("debt", "/det/", 1, []),
        ("debut", "/de\u026a\u02c8bju\u02d0/", 2, []),
        ("dessert", "/d\u026a\u02c8z\u025c\u02d0t/", 2, []),
        ("dilemma", "/d\u026a\u02c8lem\u0259/", 3, []),
        ("dossier", "/\u02c8d\u0252sie\u026a/", 3, []),
        ("drought", "/d\u0279a\u028at/", 1, []),
        ("duel", "/\u02c8dju\u02d0\u0259l/", 2, []),
        ("dungeon", "/\u02c8d\u028cnd\u0292\u0259n/", 2, []),
        ("ecstasy", "/\u02c8ekst\u0259si\u02d0/", 3, []),
        ("elite", "/\u026a\u02c8li\u02d0t/", 2, []),
        ("entrepreneur", "/\u02cc\u0252nt\u0279\u0259p\u0279\u0259\u02c8n\u025c\u02d0/", 4, []),
        ("fiery", "/\u02c8fa\u026a\u0259\u0279i\u02d0/", 2, []),
        ("gauge", "/\u0261e\u026ad\u0292/", 1, []),
        ("gist", "/d\u0292\u026ast/", 1, []),
        ("guarantee", "/\u02cc\u0261\u00e6\u0279\u0259n\u02c8ti\u02d0/", 3, []),
        ("heinous", "/\u02c8he\u026an\u0259s/", 2, []),
        ("hors d'oeuvres", "/\u0254\u02d0 \u02c8d\u025c\u02d0v\u0279\u0259/", 2, []),
        ("inevitable", "/\u026an\u02c8ev\u026at\u0259b\u0259l/", 5, []),
        ("infamous", "/\u02c8\u026anf\u0259m\u0259s/", 3, []),
        ("karate", "/k\u0259\u02c8\u0279\u0251\u02d0ti\u02d0/", 3, []),
        ("knight", "/na\u026at/", 1, []),
        ("limousine", "/\u02c8l\u026am\u0259zi\u02d0n/", 3, []),
        ("maintenance", "/\u02c8me\u026ant\u0259n\u0259ns/", 3, []),
        ("medieval", "/\u02ccmed\u026a\u02c8i\u02d0v\u0259l/", 4, []),
        ("memoir", "/\u02c8memw\u0251\u02d0/", 2, []),
        ("menace", "/\u02c8men\u0259s/", 2, []),
        ("miniature", "/\u02c8m\u026an\u026at\u0283\u0259/", 3, []),
        ("nauseous", "/\u02c8n\u0254\u02d0\u0283\u0259s/", 2, []),
        ("negotiate", "/n\u026a\u02c8\u0261\u0259\u028a\u0283ie\u026at/", 4, []),
        ("nonchalant", "/\u02c8n\u0252n\u0283\u0259l\u0259nt/", 3, []),
        ("paradigm", "/\u02c8p\u00e6\u0279\u0259da\u026am/", 3, []),
        ("parliament", "/\u02c8p\u0251\u02d0l\u0259m\u0259nt/", 3, []),
        ("perhaps", "/p\u0259\u02c8h\u00e6ps/", 2, []),
        ("phenomenon", "/f\u026a\u02c8n\u0252m\u026an\u0259n/", 4, []),
        ("pneumonia", "/nju\u02d0\u02c8m\u0259\u028ani\u02d0\u0259/", 4, []),
        ("prescription", "/p\u0279\u026a\u02c8sk\u0279\u026ap\u0283\u0259n/", 3, []),
        ("privilege", "/\u02c8p\u0279\u026avl\u026ad\u0292/", 3, []),
        ("prodigy", "/\u02c8p\u0279\u0252d\u026ad\u0292i\u02d0/", 3, []),
        ("protein", "/\u02c8p\u0279\u0259\u028ati\u02d0n/", 2, []),
        ("psychiatrist", "/sa\u026a\u02c8ka\u026a\u0259t\u0279\u026ast/", 4, []),
        ("questionnaire", "/\u02cckwest\u0283\u0259\u02c8ne\u0259/", 3, []),
        ("rapport", "/\u0279\u00e6\u02c8p\u0254\u02d0/", 2, []),
        ("raspberry", "/\u02c8\u0279\u0251\u02d0zb\u0259\u0279i\u02d0/", 3, []),
        ("regime", "/\u0279e\u026a\u02c8\u0292i\u02d0m/", 2, []),
        ("reservoir", "/\u02c8\u0279ez\u0259vw\u0251\u02d0/", 3, []),
        ("rhetoric", "/\u02c8\u0279et\u0259\u0279\u026ak/", 3, []),
        ("sabotage", "/\u02c8s\u00e6b\u0259t\u0251\u02d0\u0292/", 3, []),
        ("silhouette", "/\u02ccs\u026alu\u02d0\u02c8et/", 3, []),
        ("soldier", "/\u02c8s\u0259\u028ald\u0292\u0259/", 2, []),
        ("sovereign", "/\u02c8s\u0252v\u0279\u026an/", 3, []),
        ("spaghetti", "/sp\u0259\u02c8\u0261eti\u02d0/", 3, []),
        ("squirrel", "/\u02c8skw\u025c\u02d0\u0279\u0259l/", 2, []),
        ("succinct", "/s\u0259k\u02c8s\u026a\u014bkt/", 2, []),
        ("technique", "/tek\u02c8ni\u02d0k/", 2, []),
        ("thorough", "/\u02c8\u03b8\u028c\u0279\u0259/", 2, []),
        ("tsunami", "/tsu\u02d0\u02c8n\u0251\u02d0mi\u02d0/", 3, []),
        ("turbulence", "/\u02c8t\u025c\u02d0bj\u028al\u0259ns/", 3, []),
        ("unique", "/ju\u02d0\u02c8ni\u02d0k/", 2, []),
        ("vague", "/ve\u026a\u0261/", 1, []),
        ("venetian", "/v\u026a\u02c8ni\u02d0\u0283\u0259n/", 3, []),
        ("versatile", "/\u02c8v\u025c\u02d0s\u0259ta\u026al/", 3, []),
        ("victual", "/\u02c8v\u026at\u0259l/", 2, []),
        ("villain", "/\u02c8v\u026al\u0259n/", 2, []),
        ("visceral", "/\u02c8v\u026as\u0259\u0279\u0259l/", 3, []),
        ("whistle", "/\u02c8w\u026as\u0259l/", 2, []),
        ("wreath", "/\u0279i\u02d0\u03b8/", 1, []),
        ("xylophone", "/\u02c8za\u026al\u0259f\u0259\u028an/", 3, []),
        ("zephyr", "/\u02c8zef\u0259/", 2, []),
        ("adjective", "/\u02c8\u00e6d\u0292\u026akt\u026av/", 3, []),
        ("ache", "/e\u026ak/", 1, ["ah-cheh"]),
        ("asthma", "/\u02c8\u00e6zm\u0259/", 2, ["AST-ma"]),
        ("buffet", "/b\u028a\u02c8fe\u026a/", 2, ["BUFF-et"]),
        ("cacao", "/k\u0259\u02c8ka\u028a/", 3, []),
        ("concierge", "/\u02cck\u0252nsi\u02c8e\u0259\u0292/", 3, []),
        ("fatigue", "/f\u0259\u02c8ti\u02d0\u0261/", 2, []),
        ("mauve", "/m\u0259\u028av/", 1, []),
        ("plumber", "/\u02c8pl\u028cm\u0259/", 2, []),
        ("quiche", "/ki\u02d0\u0283/", 1, []),
        ("suede", "/swe\u026ad/", 1, []),
    ]

    def __init__(self) -> None:
        self._index: dict[str, WordPronunciation] = {}
        for word, ipa, syllables, errors in self.WORDS:
            self._index[word.lower()] = WordPronunciation(
                word=word.lower(),
                ipa=ipa,
                phonemes=[],  # Phoneme extraction delegated to PhonemeAnalyzer
                syllable_count=syllables,
                common_errors=errors,
            )

    def get(self, word: str) -> WordPronunciation | None:
        """Look up a word in the database."""
        return self._index.get(word.lower().strip())

    def search(self, prefix: str) -> list[WordPronunciation]:
        """Search for words starting with the given prefix."""
        prefix = prefix.lower().strip()
        return [wp for w, wp in self._index.items() if w.startswith(prefix)]

    def all_words(self) -> list[WordPronunciation]:
        """Return all words in the database."""
        return list(self._index.values())

    def count(self) -> int:
        """Return the number of words in the database."""
        return len(self._index)

    def words_by_syllable_count(self, n: int) -> list[WordPronunciation]:
        """Return words with exactly n syllables."""
        return [wp for wp in self._index.values() if wp.syllable_count == n]

    def words_with_errors(self) -> list[WordPronunciation]:
        """Return words that have documented common errors."""
        return [wp for wp in self._index.values() if wp.common_errors]
