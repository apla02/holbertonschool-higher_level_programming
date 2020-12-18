# 0x10 PYTHON-NETWORK-0

## General
> - What a URL is
    A Uniform Resource Locator (URL), colloquially termed a web address,[1] is a reference to a web resource that specifies its location on a computer network and a mechanism for retrieving it.

> - What HTTP is
    It is a protocol which allows the fetching of resources, such as HTML documents. It is the foundation of any data exchange on the Web and it is a client-server protocol, which means requests are initiated by the recipient, usually the Web browser.

> - How to read a URL
    Uniform Resource Locator”, defines the web address to a specific resource
    "protocol://" - This defines what Internet protocol is required to reach the online resource. Commonly used protocols include:
        http:// - Hypertext Transfer Protocol - used to access a server that is supporting the WWW protocol (i.e. web server) - commonly used for downloading web pages and associated imbedded elements
        ftp:// - File Transfer Protocol - used to download a file from a server supporting the FTP Protocol - commonly used to download a software program
        news: - Used to access a usenet newsgroup from your news server - Your web browser  must be configured to access a specific news-server
        telnet:// - Establish a telnet session ( terminal emulation) to the specified host (often a VT100 Session)
        mailto: Initiates an outgoing email message to the address specified
    "computer.domain.name" - The domain name of the server where the information is located (can also be the server's IP number) For more information, see my Domain Name Overview.  ( you may also want to read this article about domain names starting www)
    "/pathname/" - Usually consists of directory/subdirectory names. This defines where on the server's hard disk to look for the information.
    "filename.ext"

> - The scheme for a HTTP URL
    //host:port/path?query
> - What a domain name is
    an identification string that defines a realm of administrative autonomy, authority or control within the Internet
> - What a sub-domain is
    A subdomain is an additional part to your main domain name. Subdomains are created to organize and navigate to different sections of your website
> - How to define a port number in a URL
    Port numbers are sometimes seen in web or other uniform resource locators (URLs). By default, HTTP uses port 80 and HTTPS uses port 443, but a URL like http://www.example.com:8080/path/ specifies that the web browser connects instead to port 8080 of the HTTP server.
> - What a query string is
    A query string is a part of a uniform resource locator (URL) that assigns values to specified parameters.
> - What an HTTP request is
    An HTTP request is an action to be performed on a resource identified by a given Request-URL.
> - What an HTTP response is
    An HTTP response is made by a server to a client.
> - What HTTP headers are
    HTTP headers are the code that transfers data between a Web server and a client.
> - What the HTTP message body is
    Is the data bytes transmitted in an HTTP transaction message immediately following the headers if there are any
> - What an HTTP request method is
        GET: most common method to retreive information from the server (read). When you are surfing in Google or other website, your web browser is doing GET requests to each website to reteive HTML/CSS/JS etc… to render correctly the website. Client can send some information to the server via query string.
        POST: use to send datas to the server (write) contain in the request body (see below)
        HEAD: same as GET but with an empty response. It’s mainly used to check if a resource is available but without get it.
        PUT/PATCH: to update a resource with datas contain in the request body
        DELETE: to remove a resource in the server (mainly used for an RestAPI)
> - What an HTTP response status code is
        Status codes are issued by a server in response to a client's request made to the server.
> - What an HTTP Cookie is
        An HTTP cookie (web cookie, browser cookie) is a small piece of data that a server sends to the user's web browser. 
> - How to make a request with cURL
    curl -flags url
> - What happens when you type google.com in your browser (Application level)