from bert_serving.server.helper import get_args_parser
from bert_serving.server import BertServer
args = get_args_parser().parse_args(['-model_dir', 'chinese_L-12_H-768_A-12',
                                     '-pooling_strategy', 'NONE',
                                     '-max_seq_len','60'])
server = BertServer(args)
server.start()
from bert_serving.client import BertClient
bc = BertClient(ip='localhost')
test=bc.encode(['你','bert'])

a1=bc.encode(['你','bert'])

tes=', '.join(str(i) for i in test[0][0])

for i in 
f=open("test.txt", "w")
f.write(str(tes))
f.close()


with open('char_form.txt','r',encoding='utf-8') as f:#r为标识符，表示只读
    for i in f.readlines():
        infmation=bc.encode([i])
        tes=', '.join(str(i) for i in infmation[0][0])
        f=open("test.txt", "a")
        f.write(i.strip()+'  '+str(tes)+'\n')
        f.close()
        
        

    print(f.read())