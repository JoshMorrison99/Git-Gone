# Git-Gone
Bug Bounty GitHub secrets leak automation. Extracts {-25}{KEYWORD}{+50} from the following GitHub dorks:
```
"target.com" secret
"taget.com" password
```

**Usage**
```
python gitgone.py -t target.com -a {GitHub API Token}
```

**Example Input**
```
python gitgone.py -t avalara.com -a ghp_...
```

**Example Output**
```
{
   "secret":[
      [
         {
            "url":"https://raw.githubusercontent.com/killbill/killbill-avatax-plugin/12e0f06752c2313e0ff9375d760b2af5529cbc45/README.md",
            "name":"README.md",
            "extension":"md",
            "extracted":[
               [
                  "\\     -H 'X-Killbill-ApiSecret: lazar' \\     -H 'X-Killbill-CreatedBy: ad",
                  "\\     -H 'X-Killbill-ApiSecret: lazar' \\     -H 'X-Killbill-CreatedBy: ad",
                  "\\     -H 'X-Killbill-ApiSecret: lazar' \\     http://127.0.0.1:8080/plugin",
                  "\\     -H 'X-Killbill-ApiSecret: lazar' \\     http://127.0.0.1:8080/plugin",
                  "\\     -H 'X-Killbill-ApiSecret: lazar' \\     -H 'X-Killbill-CreatedBy: ad",
                  "\\     -H 'X-Killbill-ApiSecret: lazar' \\     -H 'X-Killbill-CreatedBy: ad",
                  "\\     -H 'X-Killbill-ApiSecret: lazar' \\     -H 'X-Killbill-CreatedBy: ad",
                  "\\     -H 'X-Killbill-ApiSecret: lazar' \\     -H 'X-Killbill-CreatedBy: ad",
                  "\\     -H 'X-Killbill-ApiSecret: lazar' \\     -H 'X-Killbill-CreatedBy: ad"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/cmsavalarasre/gitlab-PoC/85e2fb16478a3b71209da53df07a267baf3891a6/kubernetes.sh",
            "name":"kubernetes.sh",
            "extension":"sh",
            "extracted":[
               [
                  "RDkubectl -n qa create secret docker-registry regcred --docker-server=doc",
                  "ctl -n production create secret docker-registry regcred --docker-server=doc"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/anil-hulkapps/php-training-september/b08ef3638d339ba075896232945a0c3ec900168d/.env.example",
            "name":".env.example",
            "extension":"env",
            "extracted":[
               [
                  "AWS_ACCESS_KEY_ID=AWS_SECRET_ACCESS_KEY=AWS_DEFAULT_REGION=us-east-1AW",
                  "SHER_APP_KEY=PUSHER_APP_SECRET=PUSHER_APP_CLUSTER=mt1MIX_PUSHER_APP_KEY",
                  "IFY_API_KEY=SHOPIFY_API_SECRET=SHOPIFY_API_DOMAIN=SHOPIFY_API_RATE_LIMI"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/saleor/saleor-avatax/1f4403d7fec66c4ed90442f4a4384829c743b85d/README.md",
            "name":"README.md",
            "extension":"md",
            "extracted":[
               [
                  "- `SETTINGS_ENCRYPTION_SECRET` - used to encrypt/decrypt secret data (lik",
                  " used to encrypt/decrypt secret data (like Password) that is stored in Sale"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/msankhla/msankhla/720fb730a41e1a43dd6564e6fd1ba28170a8627c/vendor/avalara/avatax-magento/BaseProvider/Helper/Generic/Config.php",
            "name":"Config.php",
            "extension":"php",
            "extracted":[
               [
                  " * @param string $accountSecret     * @param string $accountSecret     * ",
                  " * @param string $accountSecret     * @return string     */    public fu",
                  "($accountNumber, $accountSecret)    {        return base64_encode($accoun",
                  "ntNumber . \":\" . $accountSecret);    }    /**     * Validate Record   ",
                  "ecord[\\'config\\'][\\'account_secret\\'])) {                $exception[] = \"accou",
                  " $exception[] = \"account_secret parameters is missing for API Logging.\";  "
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/avadev/Avalara-AvaTax-for-Magento2/ed4279025184a5bc58a94879336bfc511e0ea797/BaseProvider/Helper/Generic/Config.php",
            "name":"Config.php",
            "extension":"php",
            "extracted":[
               [
                  " * @param string $accountSecret     * @param string $accountSecret     * ",
                  " * @param string $accountSecret     * @return string     */    public fu",
                  "($accountNumber, $accountSecret)    {        return base64_encode($accoun",
                  "ntNumber . \":\" . $accountSecret);    }    /**     * Validate Record   ",
                  "ecord[\\'config\\'][\\'account_secret\\'])) {                $exception[] = \"accou",
                  " $exception[] = \"account_secret parameters is missing for API Logging.\";  "
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/het-hulkapps/php-training/b8b2111e41a579b82f2417e115abfa7ac7525437/.env.example",
            "name":".env.example",
            "extension":"env",
            "extracted":[
               [
                  "AWS_ACCESS_KEY_ID=AWS_SECRET_ACCESS_KEY=AWS_DEFAULT_REGION=us-east-1AW",
                  "SHER_APP_KEY=PUSHER_APP_SECRET=PUSHER_APP_CLUSTER=mt1MIX_PUSHER_APP_KEY",
                  "IFY_API_KEY=SHOPIFY_API_SECRET=SHOPIFY_API_DOMAIN=SHOPIFY_API_RATE_LIMI"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/cucucuck/11/900f5f5aba2f3127e0eff16c5bf9b90abbfd4f9b/spec/fixtures/configs/av/Avalara:developer-dot.yml",
            "name":"Avalara:developer-dot.yml",
            "extension":"yml",
            "extracted":[
               [
                  "_success:  - if [ -n \"$secret_key\" ] && [ \"$TRAVIS_BRANCH\" == \"master\" ] ",
                  "sh;    fi  - if [ -n \"$secret_key\" ] && [ \"$TRAVIS_BRANCH\" == \"staging\" ]"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/ashishbakhtar-avalara/DeveloperDot/40e70cdfe342e478679fbd11319f81631f64dbd5/.travis.yml",
            "name":".travis.yml",
            "extension":"travis",
            "extracted":[
               [
                  "a push; fi  - if [ -n \"$secret_key\" ] && [ \"$TRAVIS_BRANCH\" == \"master\" ];"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/saurabh-sali-hulkapps/php-training/af6544c6910b546841871d214c1dc442ea5eb6fa/.env.example",
            "name":".env.example",
            "extension":"env",
            "extracted":[
               [
                  "AWS_ACCESS_KEY_ID=AWS_SECRET_ACCESS_KEY=AWS_DEFAULT_REGION=us-east-1AW",
                  "SHER_APP_KEY=PUSHER_APP_SECRET=PUSHER_APP_CLUSTER=mt1MIX_PUSHER_APP_KEY",
                  "IFY_API_KEY=SHOPIFY_API_SECRET=SHOPIFY_API_DOMAIN=SHOPIFY_API_RATE_LIMI"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/jacob-ebey/golang-ecomm/9e88e660c2d435c248c073a9892c5ad37db9605d/.env.example",
            "name":".env.example",
            "extension":"env",
            "extracted":[
               [
                  "KEN=\"your-value\"# Your secret used to encode the JWT tokens.JWT_SECRET=\"",
                  "code the JWT tokens.JWT_SECRET=\"your-value\"# Used in things such as emai"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/cmsavalarasre/gitlab-PoC/85e2fb16478a3b71209da53df07a267baf3891a6/kubernetes/bin/deploy.sh",
            "name":"deploy.sh",
            "extension":"sh",
            "extracted":[
               [
                  "-n ${KUBE_NAMESPACE} get secret regcred --no-headers --output=go-template={",
                  "{KUBE_NAMESPACE}\" create secret docker-registry regcred \\            --doc"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/benfjohnson/developer-dot/1e2ce5932c14429b4efba339e2b86a627afe675e/avatax/errors/BasicAuthIncorrect.md",
            "name":"BasicAuthIncorrect.md",
            "extension":"md",
            "extracted":[
               [
                  "ase64(credential + ':' + secret)```An example header looks like this:`"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/benfjohnson/developer-dot/1e2ce5932c14429b4efba339e2b86a627afe675e/_posts/2016-10-03-new-rest-v2-api-for-avatax.md",
            "name":"2016-10-03-new-rest-v2-api-for-avatax.md",
            "extension":"md",
            "extracted":[
               [
                  "se tiny beginnings.The secret to Avalara's success is constant innovation"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/benfjohnson/developer-dot/1e2ce5932c14429b4efba339e2b86a627afe675e/.travis.yml",
            "name":".travis.yml",
            "extension":"travis",
            "extracted":[
               [
                  "a push; fi  - if [ -n \"$secret_key\" ] && [ \"$TRAVIS_BRANCH\" == \"master\" ];"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/mlsnyder/mlsnyder-devguide.github.io/e3738ee4937dbf122abad82bd3080f1efa2fd9ce/avatax/errors/BasicAuthIncorrect.md",
            "name":"BasicAuthIncorrect.md",
            "extension":"md",
            "extracted":[
               [
                  "ase64(credential + ':' + secret)```An example header looks like this:`"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/ashishbakhtar-avalara/DeveloperDot/40e70cdfe342e478679fbd11319f81631f64dbd5/avatax/errors/BasicAuthIncorrect.md",
            "name":"BasicAuthIncorrect.md",
            "extension":"md",
            "extracted":[
               [
                  "ase64(credential + ':' + secret)```An example header looks like this:`"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/mlsnyder/mlsnyder-devguide.github.io/e3738ee4937dbf122abad82bd3080f1efa2fd9ce/.travis.yml",
            "name":".travis.yml",
            "extension":"travis",
            "extracted":[
               [
                  "a push; fi  - if [ -n \"$secret_key\" ] && [ \"$TRAVIS_BRANCH\" == \"master\" ];"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/travis-ci/travis-yml/f25fae51bc8aaab4d0792c6f14d5e26435f2a9ec/spec/fixtures/configs/av/Avalara:developer-dot.yml",
            "name":"Avalara:developer-dot.yml",
            "extension":"yml",
            "extracted":[
               [
                  "_success:  - if [ -n \"$secret_key\" ] && [ \"$TRAVIS_BRANCH\" == \"master\" ] ",
                  "sh;    fi  - if [ -n \"$secret_key\" ] && [ \"$TRAVIS_BRANCH\" == \"staging\" ]"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/ordercloud-api/oc-documentation/5ac20f158429a739b5e209a224bf23a7bbc428dd/content/documents/prebuilt-checkout-integrations-in-dotnet.mdx",
            "name":"prebuilt-checkout-integrations-in-dotnet.mdx",
            "extension":"mdx",
            "extracted":[
               [
                  "m/test/apikeys) to get a secret and a publishable API key.- Edit the `.git",
                  "t as a Github repository secret with name `AZURE_WEBAPP_PUBLISH_PROFILE`. [",
                  "create-a-publish-profile-secret). This will authenticate deployments. - Ru"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/brusinow/sisters-site/43baa031e48645d4c6a76a66cb4790de0daf0079/index.js",
            "name":"index.js",
            "extension":"js",
            "extracted":[
               [
                  "ipe\")(process.env.STRIPE_SECRET);var Twitter = require(\\'twitter\\');var twi",
                  "CONSUMER_KEY,  consumer_secret: process.env.TWITTER_CONSUMER_SECRET,  acc",
                  "ess.env.TWITTER_CONSUMER_SECRET,  access_token_key: process.env.TWITTER_TO",
                  "ER_TOKEN,  access_token_secret: process.env.TWITTER_TOKEN_SECRET});app.",
                  "rocess.env.TWITTER_TOKEN_SECRET});app.use(session({  secret: process.en",
                  "});app.use(session({  secret: process.env.SESSION_SECRET,  resave: fals",
                  "ret: process.env.SESSION_SECRET,  resave: false,  saveUninitialized: true"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/ashishbakhtar-avalara/DeveloperDot/40e70cdfe342e478679fbd11319f81631f64dbd5/_posts/2016-10-03-new-rest-v2-api-for-avatax.md",
            "name":"2016-10-03-new-rest-v2-api-for-avatax.md",
            "extension":"md",
            "extracted":[
               [
                  " tiny beginnings.  The secret to Avalara's success is constant innovation"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/himadric/myheadstart/69841d6699c1593dccdf85c25ff8626d7500394b/README.md",
            "name":"README.md",
            "extension":"md",
            "extracted":[
               [
                  "Settings:MiddlewareClientSecret`. These will be returned on a successful se",
                  " middleware clientID and secret. Save these two values in your app configur",
                  "Settings:MiddlewareClientSecret`   2. The buyer clientID. Follow the instr",
                  "Settings_MiddlewareClientSecret4. From the project directory, start up you"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/mlsnyder/mlsnyder-devguide.github.io/e3738ee4937dbf122abad82bd3080f1efa2fd9ce/_posts/2016-10-03-new-rest-v2-api-for-avatax.md",
            "name":"2016-10-03-new-rest-v2-api-for-avatax.md",
            "extension":"md",
            "extracted":[
               [
                  " tiny beginnings.  The secret to Avalara's success is constant innovation"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/dominik-stripe/stripe-avatax-demos/11bcce2b4e453177af2a7626419fb7b023b14b3d/pages/api/calculate-taxes.ts",
            "name":"calculate-taxes.ts",
            "extension":"ts",
            "extracted":[
               [
                  "tripe(process.env.STRIPE_SECRET_KEY!, {  apiVersion: \"2020-08-27\",});con"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/Orckestra/CommerceModel.BetterRetail/41d129b75e0574cbfdc954505fa1a833f8c8159f/README.md",
            "name":"README.md",
            "extension":"md",
            "extracted":[
               [
                  "tId>' ; DeliverySolutionsSecretKey = '<DeliverySolutionsSecretKey>'} }```",
                  "Key = '<DeliverySolutionsSecretKey>'} }```The sensitive information (use",
                  "\",>   \"DeliverySolutionsSecretKey\": \"\"> }> ```### Before doing a Git c",
                  " = '' ; DeliverySolutionsSecretKey = '' } | A PowerShell formatted Hashtabl"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/codingblazer/C5-Kubernetes-Course/65a3af706299e41474b4910af5ccd81213e912d7/Notes/x20.%20Kubernetes%20Advanced%202",
            "name":"x20. Kubernetes Advanced 2",
            "extension":" Kubernetes Advanced 2",
            "extracted":[
               [
                  "6. ConfigMaps and Secrets------------------------------------------",
                  "plying both the files. SECRETSTo store the sensitive information like pa",
                  "-2 in same file. Using Secrets: Now if you think secrets are safe, they ",
                  "crets: Now if you think secrets are safe, they are not. It can be actually",
                  "kubectl as:'kubectl get secret aws-credentials -o yaml' and we can see it",
                  "we can add roles to this secret resource so that not everyone can access th",
                  "everyone can access this secret through kubectl command and this is somethi",
                  "ticate will be stored as secret :1. We will hash the passwords using the ",
                  "of passwordand create a secret by providing this file as:'kubectl create ",
                  "file as:'kubectl create secret generic mycredentials --from-file auth' => ",
                  "ile auth' => will create secret from this file and give any name to secret",
                  "ile and give any name to secretNow see the ingress-secure.yaml file and f",
                  "assword specified in the secrets. => we are providing type of auth = basic,",
                  "ng type of auth = basic, secrets name we gave i.e. mycredentials and just r",
                  " there is a reference to secret mycredentials in the secure file. We can cr",
                  "cure file. We can create secret by command like we did on minikube but we s",
                  "be where we created this secret and get the yaml for this created secret so",
                  "he yaml for this created secret so we can use this yaml on EC2 instance for",
                  " later on:'kubectl get secret mycredentials -o yaml' => gives the yaml th",
                  "is needed to create this secret and we will remove everything generated fro",
                  "is file and do apply the secret to create it.Now we should edit our servi"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/SimisRnD/simis-cms/f821a20b4bc00e4e67b1a85295b0e701ecbabe66/README.md",
            "name":"README.md",
            "extension":"md",
            "extracted":[
               [
                  "property_value = 'client-secret' WHERE property_name = 'oauth.clientSecret'",
                  "erty_name = 'oauth.clientSecret';UPDATE site_properties SET property_value",
                  "min, note the app id and secret key.2. Make sure the API is enabled in Sit",
                  "th2/authorize X-API-Key:<secret_key>```When authorization is obtained, t",
                  "t:8080/api/me X-API-Key:<secret_key>``````bashhttp -A bearer -a <access",
                  "calhost:8080/api/me?key=<secret_key>```Calls without a user:```bashhtt",
                  "calhost:8080/api/me?key=<secret_key>```## Customization* Content* CSS"
               ]
            ]
         }
      ]
   ],
   "password":[
      [
         {
            "url":"https://raw.githubusercontent.com/h04n6/nhom7_Joomla/ce5c09ab297a8361f55ec69686884e501eafa009/joomla/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/DST2000/bat4/ebaf066af175bb45f103f2f4c31c64f0d0dce7e0/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/p2d0/VapeLiquids/6b038bbc66bb2a9fca37ee10bf8653b418de3b9e/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/atweb-project/in-case-of.com/690f23770a3b913a47a39fd1f915cd47d5641dd3/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/aroshamudalige/Joomla-Project/7e6a675d01307be81c548b8ba01b2d83f70ca327/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/DEYBISON/pesfifa2016/f13949f8fccb47667b843f5a4001a241425cb9bd/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/justinmcunn/AvaTax-SOAP-NET-SDK/498657d6cc47df5714d63f209c349cb840397d36/Proxies/BaseSvcProxy.cs",
            "name":"BaseSvcProxy.cs",
            "extension":"cs",
            "extracted":[
               [
                  "xml' path='adapter/proxy/Password/*' />\t\t/// <remarks/>\t[ComVisible(false",
                  "lse)]\tpublic class ProxyPassword\t{\t\t/// <remarks/>\t\t[XmlAttributeAttrib",
                  "<remarks/>\t\tpublic ProxyPassword Password = new ProxyPassword();\t}\t/// ",
                  ">\t\tpublic ProxyPassword Password = new ProxyPassword();\t}\t/// <include ",
                  "word Password = new ProxyPassword();\t}\t/// <include file='BaseSvcProxy.D"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/sal-git/saleor-platform-test/a5d37906a6134aebea79b812cf742663574002e9/saleor/saleor/plugins/avatax/tests/cassettes/test_get_cached_tax_codes_or_fetch_wrong_response.yaml",
            "name":"test_get_cached_tax_codes_or_fetch_wrong_response.yaml",
            "extension":"yaml",
            "extracted":[
               [
                  "essage\":\"Field        \\'\\'password\\'\\' has an invalid length.\",\"description\":\"",
                  "\",\"description\":\"Field \\'\\'password\\'\\' must        be between 5 and 50 charac"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/thanhphong190/web_joomla/79e6aff245ff513ef7cff98c344681a9006b9067/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/pxxxxj/joomla/48e75c88ebfda56f984939b1811e631475614654/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/sam-akopyan/hamradio/789e725dde14a465206b1b2cf493b938fbe05369/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/devdemon/store_avalaratax/ad30c3faf75f22772a96cc9f71d8447312323b9d/AvaTax/DynamicSoapClient.php",
            "name":"DynamicSoapClient.php",
            "extension":"php",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/Crashoverride2002/foodsyd/41d9820eff2f28f1300637bf801074b5967344fa/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/DanielVazquez06/rikitoTienda/922f176c28535b3bc15b592d5e64d8d7ea4464cf/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/chaudharyvikrant19/lightmist/03b582c56ed5c88615514d1613400149bf53cf18/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/NaraCrls/joomla_2/0b3f0856fc19ce1284740ad1fe63877f9ff14d86/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/KavinduChamara/Joomla-Project/6103de0f9418e53136f53fbcd773fd5c719cdc88/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/JoseVG1/NE-rikito/024da40bc8b5aaf747297e9d5c811b9de5d9700c/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/b-seite/virtuemart/7393bc90d1d5d6c1a948438ae884bff25673c20e/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/paolaquiroz/myshop/9a67e93175a5a3c665fce2a2bbbfd730cae2465c/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/nadeeshi/giftshop/e25b80f1967bb4290b5fdbf3677223904019ddfd/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/FernandaBaez/ActividadFerAcademy/c1a0c6ff4c686c12ce3834d35991db0324b49964/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/Esteban1530416/ferado/5c8a737873cf89f0553ddd007cbd8c1c3f47ad8c/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/Ganusha93/clicknbuy/c891baec72103fa4f91ccd6eacbfac3ba8c26064/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/AvaCodeBear/SF_AvataxFoundationLib/221a94c8a90f1608a3e36461bf9bc18608969bec/SF_AvataxFoundationLib/src/classes/AddressSvc.cls",
            "name":"AddressSvc.cls",
            "extension":"cls",
            "extracted":[
               [
                  "}\r        public String Password {get; set;}\r        private String[] Use",
                  "        private String[] Password_type_info = new String[]{'Password','http",
                  "ype_info = new String[]{'Password','http://www.w3.org/2001/XMLSchema','stri",
                  "new String[]{'Username','Password'};\r    }\r\r    public class BaseAddress"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/Ziffity/dwellstore_community/ea9295b59e7cf12b0992c65a603db1e8d9953708/app/code/community/OnePica/AvaTax/lib/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/developerfreelancer/salecard/23d200496e0eac98fbf95bfaaa404a0d08a0ae4b/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/Sithsew/fashionPoint/abf01e748e8bd130f88a4766c51fd03207dad375/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         },
         {
            "url":"https://raw.githubusercontent.com/arlesonsilva/fortalpet/81fd4fe6616a35e348a678a1f28f5986b787aae9/plugins/vmcalculation/avalara/classes/DynamicSoapClient.class.php",
            "name":"DynamicSoapClient.class.php",
            "extension":"class",
            "extracted":[
               [
                  "                  \\'<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004",
                  "ername-token-profile-1.0#PasswordText\">\\'.$this->config->license.\\'</wsse:Pas",
                  ">config->license.'</wsse:Password>'.                    //<wsu:Created xml"
               ]
            ]
         }
      ]
   ]
}
```
