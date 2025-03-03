# Ad & Tracking Domain Regex for Cloudflare DNS Firewall

This repository provides a comprehensive regex filter that matches many common domains used for serving advertisements, tracking users, and delivering analytics. Use this regex in your Cloudflare Zero Trust DNS firewall rules to block (or monitor) traffic to these domains and improve your network’s security and privacy.

> **Warning:** Blocking some domains may impact website functionality (for example, many sites rely on Google services). Test this rule in a controlled environment before deploying it broadly.

## Regex Filter

Below is the complete regex group that combines tokens from both a sample list and additional commonly seen ad, tracking, and analytics substrings:

```regex
(advert|adserv|adsystem|admob|ads\.youtube|adsense|adservice|advertisercommunity|advertiserscommunity|adwords|adwordsexpress|app-measurement|doubleclick|2mdn|google-analytics|googleadapis|googleads|googleadservices|googleadsserving|googleoptimize|googlesyndication|googletagmanager|googletagservices|googletraveladservices|googlevads|mail-ads\.google|marketingplatform\.google|urchin|truecaller|uberads|206ads|360in|360yield|3lift|a2z|aarki|ad2iction|adcolony|addthis|adform|adhaven|adlooxtracking|admicro|adnxs|adpushup|adroll|adsafeprotected|adsbynimbus|adspruce|adsrvr|adswizz|adtelligent|adventori|adzerk|aerserv|amplitude|aniview|anzuinfra|apester|aralego|atdmt|atwola|bannersnack|batmobi|bluecava|blueconic|carambo|casalemediacriteo|crittercismriteo|crittercism|revcontent|ijinshan|imrworldwide|inmobi|marketo|moatads|moatpixel|mookie|perfectaudience|permutive|pubmatic|pushwoosh|rayjump|revjet|rfihub|richrelevance|rqmob|rubiconproject|onetag|samba|scopely|scorecardresearch|shareaholic|sharethis|sharethrough|smaato|snapads|speedshiftmedia|supersonicads|swrve|taboola|tremorhub|unity3d|vertamedia|videohub|vungle|wzrkt|xiaomi|yieldlove|yieldmo|yieldoptimizer|baidu|chinanet|yandex)
```

## How to Add This Regex to Cloudflare DNS Firewall Rules

Follow these steps to add the regex to your Cloudflare Zero Trust DNS firewall:

1. **Log in to Cloudflare Zero Trust Dashboard**  
   Open your Cloudflare Zero Trust portal.

2. **Navigate to Gateway > Firewall Policies**  
   In the sidebar, click on **Gateway** and then select **Firewall policies**.

3. **Add a New Policy**  
   In the **DNS** tab, click **Add a policy**.

4. **Name Your Policy**  
   Give your policy a descriptive name (e.g., *"Block Ad & Tracking Domains"*).

5. **Build the Logical Expression**  
   Under the **Traffic** section, create a rule by setting:
   
   - **Selector:** Domain  
   - **Operator:** Matches Regex  
   - **Value:** Paste the complete regex provided above
   
   For example, your rule should look similar to:

   | Selector | Operator      | Value (Regex)                                                                | Action |
   |----------|---------------|-------------------------------------------------------------------------------|--------|
   | Domain   | Matches Regex | *(paste the entire regex above)*                                             | Block  |

6. **Choose an Action**  
   Set the action to **Block** (or choose another action, such as Log, if you prefer to monitor traffic).

7. **Create the Policy**  
   Click **Create policy** to save and activate your new DNS firewall rule.

For more detailed guidance, refer to [Cloudflare DNS Policies documentation](https://developers.cloudflare.com/cloudflare-one/policies/gateway/initial-setup/dns/#3-create-your-first-dns-policy).

## Customization and Maintenance
  
- **Updating:**  
  Update the regex as needed when new ad or tracking domains emerge. You can add or remove tokens based on your network’s requirements.
