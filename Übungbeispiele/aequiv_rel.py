class Mod5:
      def __init__(self,zahl):
          self.zahl=zahl
      def __eq__(self,other):
          return (self.zahl-other.zahl)%5==0

