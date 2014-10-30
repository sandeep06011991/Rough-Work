class element:
	def __init__(self,parent,data):
		self.rht=0
		self.lht=0
		self.data=data
		self.ht=1
		self.hb=0
		self.rch=None
		self.lch=None
		self.parent=parent
		
		
class awl:
	def __init__(self):
			self.root=None
	def insert(self,node,data):
		parent=node
		while(node!=None):		
			parent=node
			if(node.data>data):
				node=node.lch
			else:
				node=node.rch
		if parent==None:
			self.root=element(None,data)
		else:
			node=element(parent,data)
			if parent.data>data :
				parent.lch=node
				
			else:
				parent.rch=node
		self.postorder(self.root)
		self.rebalance(node)
		self.postorder(self.root)					
	def ins(self,data):
		self.insert(self.root,data)
	def inorder(self,node):#plain inorder traversal
		if node==None: return
		self.inorder(node.lch)
		print node.data , node.ht , node.hb
		self.inorder(node.rch)
	def postorder(self,node):#refreshes the heights of all the nodes
		if node==None: return
		self.postorder(node.lch)
		self.postorder(node.rch)
		def ht(nd):
			if nd==None: return 0
			return nd.ht
		if(ht(node.rch)>ht(node.lch)):
			node.ht=ht(node.rch)+1
		else:
			node.ht=ht(node.lch)+1
		node.hb=(ht(node.rch)-ht(node.lch))**2
	def rebalance(self,node):# finds first node of imbalance and maps the rotation plan
		if node ==None: return
		while(node.hb!=4):
			node=node.parent
			if node ==None : return
		
		
		if (self.ht(node.lch)>self.ht(node.rch)):
				ch1=node.lch
				x=-1
		else:
			ch1=node.rch
			x=+1
		if (self.ht(ch1.lch)>self.ht(ch1.rch)):
				ch2=ch1.lch
				y=-1
		else:
			ch2=ch1.rch
			y=+1
		if(x*y==1):	
			nd=self.rotate(node,ch1)
		else:
			self.rotate(ch1,ch2)
			nd=self.rotate(node,ch2)		
		self.rebalance(nd)
	def rotate(self,nd1,nd2):# where nd1 is parent of nd2
		if(nd1.lch==nd2):
			d2=nd1.parent
			nd1.lch=nd2.rch
			nd1.parent=nd2
			nd2.rch=nd1
			nd2.parent=d2
			if d2==None: 
				self.root=nd2
			else:
				if(d2.lch==nd1):
					d2.lch=nd2
				else:
					d2.rch=nd2
			if(nd1.lch!=None):
				nd1.lch.parent=nd1
		else:
			d2=nd1.parent
			nd1.rch=nd2.lch
			nd1.parent=nd2
			nd2.lch=nd1
			nd2.parent=d2
			if d2==None: 
				self.root=nd2
			else:
				if(d2.lch==nd1):
					d2.lch=nd2
				else:
					d2.rch=nd2
			if(nd1.rch!=None):
				nd1.rch.parent=nd1	
		self.refreshht(nd1)
		self.refreshht(nd2)		
		return nd2			
	def ht(self,node):#use this to get ht of null nodes as well
			if node==None:
				 return 0
			else:
				return node.ht
	def delete_node(self,e):
		
		nd=self.find(e)
		nd=self.getleaf(nd)
		nd=self.remove(nd)# remove leaf
	def find(self,e):
		nd=self.root
		while(nd!=None) and nd.data!=e :
			if (nd.data<e):
				nd=nd.rch
			else:
				nd=nd.lch

		return nd
	def getleaf(self,nd):
		if(nd.rch ==None and nd.lch==None ): return nd
		if(nd.lch==None) :
					nd.data=nd.rch.data
					return nd.rch
		if(nd.rch==None):
					nd.data=nd.lch.data
					return nd.lch
		return self.getleaf(self.predessor(nd))
	def predessor(self,node):
		rs=node.lch
		while(rs.rch!=None):
			rs=rs.rch
		node.data=rs.data	
		return rs				
	def remove(self,nd):
		p=nd.parent
		if nd.parent.lch==nd:
			p.lch=None
		else:
			p.rch=None
		self.postorder(self.root)	
		self.rebalance(p)		
		
	def refreshht(self,node):
		if node==None : return 
		if(self.ht(node.rch)>self.ht(node.lch)):
							node.ht=self.ht(node.rch)+1
		else:
			node.ht=self.ht(node.lch)+1
		node.hb=(self.ht(node.rch)-self.ht(node.lch))**2						
if __name__=="__main__":
	tree=awl()
	for i in range(1,8):
		tree.ins(i)
	#tree.inorder(tree.root)
	#tree.delete_node(2)
	#tree.delete_node(4)
	
	#print "Seperator"
	tree.inorder(tree.root)
	
