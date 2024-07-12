from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, UnexpectedAlertPresentException, ElementClickInterceptedException, TimeoutException, WebDriverException

class App:
    def __init__(self):
        
        self.urls = [
            # "http://fit.trianh.edu.vn/phong-thi-nghiem-an-toan-thong-tin/",  
            # "https://www.golfonline.sk/odborne-clanky/greenkeeping/plesen-snezna-a-plesen-snezna-siva/", 
            # "https://mru.home.pl/produkt/afriso-tm8-ir/#reviews",
            "https://www.fivereasonssports.com/news/4-types-of-candy-most-adults-will-like/",
            # "https://www.lizsteel.com/a-new-favourite-teapot-to-sketch/",
            # "https://www.neobienetre.fr/forum-bien-etre-medecines-douces-developpement-personnel/topic/play-game-for-fun/",
            # "https://bulevard.bg/interviews/ivaylo-zahariev-v-ekskluzivno-intervyu-19.html",
            # "https://www.thelowdownblog.com/2018/03/riding-in-smartphone-powered-self.html",
            # "https://vocal.media/lifehack/mindful-music",
            # "https://www.blendermarket.com/posts/contours-polystrips-combined?page=3",
            # "http://forum.asustor.com/viewtopic.php?f=130&p=15901&t=5143",
            # "https://ged.com/insession/new-employers-offering-gedworks_august2021/",
            # "https://my.rosenbauer.com/en-US/forums/support-forum/79de424e-174e-ee11-a81c-6045bd9b2daa",
            # "https://oc-130-162-82-44.compute.oraclecloud.com/article/news/parliament/2022/joint-parliamentary-committee-against-electricity-tariff-hike",
            # "https://petrolicious.com/articles/why-the-chevrolet-chevelle-is-collectable",
            # "https://www.goldenline.pl/grupy/Literatura_kino_sztuka/wiadomosci-literackie/nominowani-do-nike,3518133/",
            # "https://www.producthunt.com/stories/is-temu-legit-safe-or-scam-what-is-temu-why-is-temu-so-cheap",
            # "https://www.todotest.com/foros/msg.asp?m=971485",
            # "https://castbox.fm/channel/Cover-Stories-with-Chess-Life-id3530473",
            # "https://cmm.bristol.ac.uk/forum/viewtopic.php?t=2366",
            # "https://community.articulate.com/discussions/building-better-courses/image-boundary",
            # "https://forum.cryengine.com/search.php?author_id=663021&sr=posts",
            # "https://support.brightsign.biz/hc/en-us/articles/218065907-Which-factors-can-affect-synchronization-",
            # "https://xarxanet.org/comment/reply/156285/253294",
            # "http://dm2ch.s59.xrea.com/cgi-bin/diary/diary.cgi?category&category_all&id=andrerushell&mode=disp&time=1580904630&writer_all",
            # "http://gritgoing.umbc.edu/tuition-remission-for-faculty-staff-2/",
            # "http://www.mynissanleaf.com/viewtopic.php?t=34352",
            # "https://musescore.org/es/node/280408",
            # "https://plarium.com/forum/en/sparta-war-of-empires/131_news-and-announcements/33260_online-chat-with-plarium-s-community-manager--5/",
            # "https://www.careerguide.com/ask/t/i-want-to-deactivate-this-account-sorry",
            # "http://blog.twinspires.com/2013/10/twinspires-horse-racing-podcast-wderek_16.html",
            # "http://blogs.socsd.org/aobrien/bridge-design-tips/comment-page-1/",
            # "http://mandelberger.cineuropa.org/2009/11/new-home-for-international-cinema.html",
            # "https://blogs.zeiss.com/news/messtechnik-de/vereinfachen-sie-sich-die-arbeit/",
            # "https://forum.wearedevs.net/t/33342",
            # "https://healingxchange.ning.com/forum/topics/how-to-handle-a-shein-package-missing?commentId=2228296%3AComment%3A1960263",
            # "https://www.inkitt.com/groups/59",
            # "https://www.saphirnews.com/forum/Completely-color-blind_m262721.html",
            # "http://bensteadwww.trustlink.org/Ask-The-Community/Question/Products/The-bond-market-is-undeniably-the-biggest-security-market-worldwide-httpswwwrevount-13473",
            # "http://feettothefire.blogs.wesleyan.edu/2009/02/26/main-street-marketplace/comment-page-2/",
            # "http://park8.wakwak.com/~w22/cgi-bin/best/read.cgi?no=2438",
            # "http://www.arwen-undomiel.com/forum/viewtopic.php?p=1233418",
            # "http://www.thinkgrowgiggle.com/2020/03/a-simple-way-to-teach-students-to-make.html",
            # "https://bergschenhoek.startpagina.nl/forum/topic/376028/goedkoop-op-vakantie/",
            # "https://blog.playerauctions.com/league-of-legends/best-ahri-build-and-guide/",
            # "https://blogs.deusto.es/innovandis/iceberg-visual-consulting-javier-miguel-garay/",
            # "https://c.cari.com.my/portal.php?aid=216591&mod=view",
            # "https://mathedu.hbcse.tifr.res.in/forums/reply/32936/",
            # "https://mojtv.hr/forum/tema/4/15094/1/the-last-of-us.aspx",
            # "https://www.apotekaonline.rs/de/blog/Sonnenallergien-Vorbeugung-Pflege-und-Behandlung",
            # "https://www.askmefast.com/I_forgot_my_textNow_password_and_I_cant_remember_the_email_I_used_when_I_signed_up_How_do_I_change_my_password_for_my_textnow_account_on_my_ipod-qna2570357.html",
            # "https://www.franklloydwrightovernight.net/forum/europe/essay-6",
            # "https://www.mtgnexus.com/customcards/4035-starcraft/24683-siege-tank-siege/",
            # "https://www.vaybee.de/00fe4be06b0996140be4f72cc87e673b/forum/showthread.php?t=14855",
            # "http://forum.e-day.kdarek.webd.pl/viewtopic.php?f=46&p=1132444&t=7406",
            # "http://lj.rossia.org/users/raskidailo/86143.html?nc=5",
            # "http://lpm-sinarfkip.trunojoyo.ac.id/2022/04/inkarnasi-neraka-dalam-sebuah-cerita.html",
            # "http://rpc.comunio.de/external/phpBB2/posting.php?mode=quote&p=5231126",
            # "https://blendedlearning.bharatskills.gov.in/mod/forum/discuss.php?d=1987",
            # "https://blogg.improveme.se/martinveltz/2014/05/27/fodboldmappen/",
            # "https://cmm.bris.ac.uk/forum/viewtopic.php?t=2366",
            # "https://community.zyxel.com/en/discussion/16223/kyrgyz-retailer-s-network-equipment-yet-to-fail-once-for-8-years",
            # "https://crabgrass.riseup.net/estado/harvey-d-breve-historia-del-neoliberalismo+374331",
            # "https://developer.tobii.com/community-forums/members/marshatel/",
            # "https://en.everybodywiki.com/Brain_train",
            # "https://fsasoutheast.boardhost.com/viewtopic.php?id=2598",
            # "https://gotartwork.com/Blog/mors-alfabesi-bileklik/133364/",
            # "https://m.swap-bot.com/swap/show/40387",
            # "https://meidan.seinajoki.fi/processes/osbu-2022/f/3/proposals/57?commentId=12243",
            # "https://support.captureone.com/hc/en-us/community/posts/11320792575261-Pro-Standard-for-Leica-Q2",
            # "https://www.canadiangunnutz.com/forum/showthread.php/1561709-forgot-password",
            # "https://www.gloria.fi/comment/reply/4639",
            # "https://www.hanaromartonline.com/forum/customer-service/amerisave-company-information",
            # "https://www.immihelp.com/forum/international-student-insurance/172405-suggestion-for-right-insurance-for-students",
            # "https://www.windsor.gov.uk/ideas-and-inspiration/blog-latest-news/read/2022/02/celebrating-the-platinum-jubilee-with-castle-hill-a-new-beer-from-windsor-and-eton-brewery-b74",
            # "http://ignites.cloud-line.com/blog/2014/06/15128/",
            # "http://notebookclub.org/forum/thread-5780.html",
            # "http://www.utilecopii.ro/forum/index.php?p=1784495&showtopic=23433&st=0",
            # "https://bogotamihuerta.jbb.gov.co/Foros/topic/how-to-fall-in-love-again-with-your-ex-lover-try-someday27790324557/",
            # "https://forum.lostcontinent.net/forum/main-forum/announcements/general/12709-what-is-the-strongest-combination-for-honkai-star-rail",
            # "https://forums.audioholics.com/forums/threads/earthquake-subwoofers.127675/",
            # "https://geekhack.org/index.php?topic=99897.0",
            # "https://groupda.com/telegram-channel/cyber-security-telegram-group-link-join-2023-join-our-group-to-learn-about-cyber-security/",
            # "https://participa.vilanova.cat/processes/ciutatesportiva/f/88/meetings/59?commentId=1156",
            # "https://participons.noisylegrand.fr/processes/budget-participatif/f/18/proposals/125?commentId=366",
            # "https://support.revvitysignals.com/hc/en-us/community/posts/6652069928852-ChemDraw21-Atom-Properties-missing-items",
            # "https://web2.0calc.com/answers/page/13700",
            # "https://www.brewology.com/forum/viewtopic.php?f=152&p=226501&t=42683",
            # "https://www.britishlogcabins.com/forum/welcome-to-the-forum/5-tips-for-acquiring-cyber-talent-in-2020",
            # "https://www.chevalannonce.com/forums-13140770-avis-selle-svp",
            # "https://www.do3d.com/forum/request-3d-models/how-about-the-constantine-holy-shotgun",
            # "https://www.ignitiondrawing.com/blog/Learn-from-the-Pros/PgrID/385/PageID/1/artmid/384/articleid/8/categoryid/3/categoryname/Views/User/Views/User/Views/User/NewRegistration",
            # "https://www.lovebakesgoodcakes.com/irish-soda-muffins/",
            # "https://www.mut.gg/forums/forum/gameplay-discussion-16/topic/which-games-count-as-house-rules-25778/",
            # "https://www.sputnikmusic.com/soundoff.php?albumid=210662",
            # "http://blog.biotecnika.org/2021/02/govt-food-analyst-recruitment-2021-rs.html",
            # "http://europenews.ki.com/2011/01/associated-architects.html",
            # "http://forum.debki.pl/viewtopic.php?p=178008",
            # "http://impulse.sakura.tv/pawanext/cgi-bin/song/read.cgi?l=1-&mode&no=5643",
            # "http://kenya.blog.malone.edu/2013/06/becca-wanjiku-bankert_7.html",
            # "http://materi-it.unpkediri.ac.id/2012/12/materi-bahasa-indonesia_30.html",
            # "http://nogg.se/Page.asp?idHomepage=37461&idPage=20128&idPageCategory=9503",
            # "http://thetortoisetable.org.uk/siteassets/forum/viewtopic.php?t=2718",
            # "http://www.dolcementeinventando.com/2018/12/gelatina-di-vin-brule.html",
            # "http://www.motot.net/forum/viewtopic.php?f=12&t=91323",
            # "http://www.old.comune.monopoli.ba.it/ServiziOnline/BachecaPiccoliAnnunci/tabid/120/fbType/View/FeedbackID/11107/language/en-US/Default.aspx",
            # "https://300hours.com/f/cfa/level-1/t/best-android-study-app-to-supplement-studying/",
            # "https://beachdriveinn.yawcam.com/forum/viewtopic.php?t=3006",
            # "https://bemorepanda.com/en/customer/6457_panda_9995?popular=1"
        ]
        
        self.selectors = {
            "author": [
                "input[type='text'][name*='author' i]",
                "input[type='text'][name*='name' i]", 
                "input[name*='name' i]",
                "input[id*='name' i]",
                "input[type='text']"],
            "email": [
                "input[type='text'][name*='mail' i]", 
                "input[name*='mail' i]", 
                "input[id*='mail' i]",
                "input[type='email']"],
            "phone": [
                "input[type='text'][name*='url' i]",  
                "input[name*='url' i]",
                "input[type='text']"],
            "comment": [
                "textarea[name*='comment' i]", 
                "input[type='text'][name*='comment' i]",  
                "input[name*='comment' i]",
                "textarea",
                "input[type='text']"],
            "submit": [
                "input[type='submit'][name*='submit' i]", 
                "input[type='submit']", 
                "input[name*='submit' i]",
                "span"]
        }

        # Initialize the Chrome WebDriver 
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.sensors": 2})
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--accept_insecure_certs")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--allow-insecure-localhost")
        chrome_options.add_argument("--ignore-certificate-errors")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.total = 0
        self.passed = 0

    def run(self):
        try:
            for url in self.urls:
                self.total += 1
                print("passed ", self.passed, "/", self.total)
                try:
                    # Open the website
                    self.driver.get(url)

                    WebDriverWait(self.driver, 1)

                    # Check if CAPTCHA is present (example: looking for a CAPTCHA element)
                    if self.is_captcha_present():
                        print("CHECK URL ", url)
                        continue

                    try:
                        # Find the comment form elements using selectors
                        name_field = self.find_element_by_any_selector(self.selectors["author"])
                        email_field = self.find_element_by_any_selector(self.selectors["email"])
                        phone_field = self.find_element_by_any_selector(self.selectors["phone"])
                        comment_box = self.find_element_by_any_selector(self.selectors["comment"])
                        submit_button = self.find_element_by_any_selector(self.selectors["submit"])

                        if not all([comment_box, name_field, email_field, phone_field, submit_button]):
                            print("nothing")
                            continue
                        else:
                            if name_field:
                                name_field.send_keys("Nhu")
                            if email_field:
                                email_field.send_keys("nhu@shemail.com")
                            if phone_field:
                                phone_field.send_keys("0398748129")
                            if comment_box:
                                comment_box.send_keys("Hello world.")
                        
                            # Submit the comment
                            if submit_button:
                                submit_button.click()
                    except ElementClickInterceptedException as e:
                        print(f"Cant click submit button {url}: {e}")
                        continue

                    except ElementNotInteractableException as e:
                        print(f"Failed to interact with element on {url}: {e}")
                        continue

                    except WebDriverException as e:
                        print(f"Connection timeout {url}: {e}")
                        continue

                except (TimeoutException) as e:
                    print(f"Page load failed on URL {url}: {e}")
                    continue
                except UnexpectedAlertPresentException:
                    print(f"Unexpected alert encountered on URL {url}")
                    continue
                except WebDriverException as e:
                    print(f"Connection timeout {url}: {e}")
                    continue
                print(f"PASSED {url}")
                self.passed += 1

        finally:
            # Close the browser session
            print("finished ", self.passed)
            self.driver.quit()

    def find_element_by_any_selector(self, selectors):
        for selector in selectors:
            try:
                element = self.driver.find_element(By.CSS_SELECTOR, selector)
                if element and element.is_displayed() and element.is_enabled():
                    return element
            except Exception as e:
                print(f"Failed to find element with selector {selector}: {e}")

    def is_captcha_present(self):
        try:
            # Example: Check for CAPTCHA element presence by some unique identifier
            captcha_element = self.driver.find_element(By.ID, "captcha-element-id")
            return True
        except NoSuchElementException:
            return False

if __name__ == "__main__":
    App().run()