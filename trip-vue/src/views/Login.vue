<template>
  <div id="login">
    <div class="sign-div">
      <h1>LOG IN</h1>
      <input class="sign-text" v-model="uid" type="text" placeholder="Full Name" >
      <input class="sign-text" v-model="password" type="password" placeholder="password">
      <input class="sign-btn" type="submit" value="Submit" @click="submit">
      <input class="sign-btn" type="submit" value="Cancel" @click="cancel">
      <a href="#">Create Account</a>
    </div>
  </div>
</template>
<script>
export default {
  data() {
      return {
        uid:'',
        password:''
      }
  },
  created() {
    console.log(this.$route);
  },
  methods:{ 
    cancel() {
    },
    submit() {
      console.log(this.uid);
      this.$store.commit('getusername',this.uid)
      this.$router.push('/')
      
    }
  }
}
</script>
<style>
  #login {
    width: 100%;
    height: 100vh;
    background-color: rgb(23, 23, 23);
  }
  .sign-div {
    position: fixed;
    z-index: 4;
    /* display: none; */
  }
  .sign-div{
    width: 300px;
    padding: 20px;
    text-align: center;
	  background: rgb(111, 7, 7) linear-gradient( rgba(0,255,0,0), rgba(170, 255, 0, 0.5));
    position:absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    overflow: hidden;
    border-radius: 50px;
}
.sign-div h1{
    margin-top: 50px;
    color: #fff;
    font-size: 40px;
}
.sign-div input{
    display: block;
    width: 100%;
    padding: 0 16px;
    height: 44px;
    text-align: center;
    box-sizing: border-box;
    outline: none;
    border: none;
    font-family: "montserrat",sans-serif;
}
.sign-text{
    margin:4px;
    background: rgba(255,255,255,5);
    border-radius: 6px;
}
.sign-btn{
    margin-top: 20px;
    margin-bottom: 20px;
    background: #487eb0;
    color: #fff;
    border-radius: 44px;
    cursor: pointer;
    transition: 0.8s;
}
.sign-btn:hover{
    transform:scale(0.96);
}
.sign-div a{
    text-decoration: none;
    color: #fff;
    font-family: "montserrat", sans-serif;
    font-size: 14px;
    padding: 10px;
    transition: 0.8s;
    display: block;
}
.sign-div a:hover{
    background: rgba(0,0,0,.3);
}
</style>