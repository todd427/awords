Great thinking! The **most popular email apps** (worldwide, consumer & business) are:

---

## **Most Popular Email Apps (2025 snapshot)**

### **For Desktop**

* **Microsoft Outlook** (Windows/Mac, huge corporate and personal market share)
* **Apple Mail** (default on all Macs, very popular with creative/pro users)
* **Mozilla Thunderbird** (powerful, open-source, popular with tech-savvy and privacy-conscious users)

### **For Web**

* **Gmail (Web/Android/iOS)** (Google’s platform dominates personal/consumer, huge worldwide user base)
* **Outlook.com** (Web, Microsoft’s consumer brand)

### **For Mobile**

* **Apple Mail (iOS)**
* **Gmail app (iOS/Android)**
* **Outlook app (iOS/Android)**

---

## **Integration Prioritization**

### **Top Priority for Extraction/Integration**

1. **Gmail (Google)**

   * Massive global user base, well-documented APIs, easy OAuth, export as MBOX/EML, great for consumer and many professionals.
2. **Microsoft Outlook/Exchange**

   * Corporate standard, huge in business; supports .pst export, EWS, Graph API.
3. **Apple Mail**

   * Strong Mac user base; stores as .eml or .mbox, easy to script or export.
4. **Thunderbird**

   * Open-source, strong privacy reputation, MBOX or EML, easy for power users.
5. **IMAP/Generic**

   * Covers a wide variety of smaller services; often “just works” for export but may be harder for users to script.

---

### **Strategic Recommendation**

**First email integration after MVP:**

* **Gmail**—by far the most popular single email platform, both via web and app.

  * Google APIs let users “Connect Gmail,” and you can pull all sent mail (with permission), apply cleaning, and build a workflow almost all users can understand.

**Next:**

* **Outlook/Exchange**

  * Especially if you want business/enterprise or older demographic.

**Third:**

* **Apple Mail and IMAP**

  * Especially for privacy/creative and older Mac-centric audiences.

---

## **Why Gmail First?**

* **Largest user base**—over 1.8 billion users worldwide.
* **Best-documented API**—robust, secure, OAuth2, plenty of sample code.
* **Easy onboarding**—users know how to grant access and revoke it.
* **Export option**—even without API, users can export all mail via Google Takeout.

---

## **Bottom Line:**

* **Build MVP for your own workflow and power users first (Thunderbird, IMAP, etc.).**
* **Gmail integration is “must-have” for mainstream/next phase.**
* **Outlook and Apple Mail should be next for maximum reach.**

---

**Want an outline for Gmail API onboarding, or a user flow for “Connect Your Gmail” in AfterWords?**
Or a roadmap for supporting Outlook and Apple Mail after that?
Let me know where you want to start!
