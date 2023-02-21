#include <iostream>
using namespace std;
class Vertex
{
	Vertex(v)
	{
		int inNeighbor[10]={3,4,5,8,32,64,74,86,90,95};
		int outNeighbor[10]={3,4,5,8,32,64,74,86,90,95};
	}
	public:
		bool hasInNeighbor(v)
		{
			for(int i=0;i<inNeighbor.length;i++)
			{
				if (v==inNeighbor)
				{
					return true;
				}
			}
			return false;
		}
		bool hasOutNeighbor(v)
		{
			for(int i=0;i<outinNeighbor.length;i++)
			{
				if (v==outNeighbor)
				{
					return true;
				}
			}
			return false;
		}
		
		bool hasNeighbor(v)
		{
			for(int i=0;i<outinNeighbor.length;i++)
			{
				if (v==outNeighbor or v==inNeighbor )
				{
					return true;
				}
			}
			return false;
		}
		void addOutNeighbor(self,v)
		{
			outNeighbors.append(v)
    	}
    
    	void addInNeighbor(self,v)
    	{		
        	inNeighbors.append(v)
   		}
};
main()
{
	
	
}


