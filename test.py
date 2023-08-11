# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 07:42:59 2023

@author: duynd
"""
from functions import *
def helloworld():
    """
Dummy Test function
    """
    print("Hello World!")


def main():
    print("Running main ()")
    text= "The Oosterschelde, a traditional EU three-masted Dutch schooner, plans to retrace the route taken by another historic ship almost two centuries ago. In Plymouth on Boxing Day 1831, a young man boarded HMS Beagle and the following day set out on a voyage that would change our world. Not that the 22-year-old Charles Darwin suspected the vast significance the voyage would later have. He was suffering a little of what would later be known as impostor syndrome, wondering if he deserved the opportunity given. Fortunately for us, however, he had the necessary determination and enthusiasm. And that is what Darwin200 founder Stewart McPherson hopes will be the legacy of this project. “We are identifying 200 young naturalists from 200 countries who will become the leaders of the future – young people who can drive change.” En route, the Oosterschelde will touch places as far apart as Cape Verde, Rio, Auckland and Tasmania – all spots Darwin reached.";
    text = '<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/structured-issues-613adf1b1211.js"></script>'
    print(Stricttext2lemmaList(text))    
if __name__ == "__main__":
    main()
