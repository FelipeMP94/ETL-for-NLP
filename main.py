from extract import Extractor, prepare_links
from transform import create_objects
from load import save_jason


if __name__ == '__main__':
    extractor = Extractor()
    extractor.extract_links_class()
    links = extractor.prepare_links()
    print(links)
   
   
 