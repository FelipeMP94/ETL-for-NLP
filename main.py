from extract import extract_links, prepare_links
from transform import create_objects
from load import save_jason


if __name__ == '__main__':
   links = prepare_links()
   obj = create_objects(links)
   print(f'Quantidade de tribunas enviadas: {len(obj)}')
   save_jason(obj)
   
 