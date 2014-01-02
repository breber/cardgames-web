CARDGAMES_ANDROID=$(pwd)/../cardgames/CardGames
LIB_VERSION=1.17.0-rc

# Generate the Java client library
endpointscfg.py get_client_lib java -o . api.CardGamesApi

# Unzip the generated zip
mv cardgames-v1.zip /tmp/CardGamesApi.zip
pushd /tmp/
yes | unzip CardGamesApi.zip
pushd cardgames

# Remove existing Jars from the libs folder of Android app
rm $CARDGAMES_ANDROID/CardGames/libs/google-*
rm $CARDGAMES_ANDROID/CardGames/libs/gson-*
rm $CARDGAMES_ANDROID/CardGames/libs/jsr*

# Copy new jars to the Android app
cp libs/gson-*.jar $CARDGAMES_ANDROID/CardGames/libs/
cp libs/jsr*.jar $CARDGAMES_ANDROID/CardGames/libs/
cp libs/google-api-client-$LIB_VERSION.jar $CARDGAMES_ANDROID/CardGames/libs/
cp libs/google-api-client-android-$LIB_VERSION.jar $CARDGAMES_ANDROID/CardGames/libs/
cp libs/google-http-client-$LIB_VERSION.jar $CARDGAMES_ANDROID/CardGames/libs/
cp libs/google-http-client-android-$LIB_VERSION.jar $CARDGAMES_ANDROID/CardGames/libs/
cp libs/google-http-client-gson-$LIB_VERSION.jar $CARDGAMES_ANDROID/CardGames/libs/
cp libs/google-oauth-client-$LIB_VERSION.jar $CARDGAMES_ANDROID/CardGames/libs/

# Get the java files out of the generated Jar
mv *.jar worthwhile-games-cardgames.zip
unzip worthwhile-games-cardgames.zip

cp -R com/appspot/* $CARDGAMES_ANDROID/CardGames/src/main/java/com/appspot/

popd # cardgames
popd # /tmp/

# Clean up after ourselves
rm /tmp/CardGamesApi.zip
rm -rf /tmp/cardgames
