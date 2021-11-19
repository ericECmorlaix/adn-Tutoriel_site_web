def define_env(env):
      "Toto's hook"

      @env.macro
      def hello() :
          return "**Demat d'an holl**<br>_Toto est dans la place !_"